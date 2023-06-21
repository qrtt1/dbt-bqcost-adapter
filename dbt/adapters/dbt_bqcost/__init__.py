import dbt.flags
from typing import Tuple

import json

import agate
from dbt.adapters.base import AdapterPlugin
from dbt.adapters.bigquery import BigQueryConnectionManager, BigQueryCredentials
from dbt.adapters.bigquery.connections import BigQueryAdapterResponse
from dbt.adapters.factory import FACTORY

from dbt.adapters.dbt_bqcost.connections import (
    dbt_bqcostConnectionManager,
    dbt_bqcostCredentials,
)  # noqa
from dbt.adapters.dbt_bqcost.impl import dbt_bqcostAdapter
from dbt.include import bigquery


class HackedAdapterPlugin(AdapterPlugin):
    def __init__(self, adapter, credentials, include_path: str, dependencies=None):
        super().__init__(adapter, credentials, include_path, dependencies)

    def __getattribute__(self, item):
        if item == "credentials":
            if "bigquery" not in FACTORY.plugins:
                FACTORY.load_plugin("bigquery")
            FACTORY.plugins["dbt_bqcost"] = FACTORY.plugins["bigquery"]
        return super().__getattribute__(item)


class Patched:
    def to_dict(self, response: BigQueryAdapterResponse) -> dict:
        return {
            "dbt_project_name": self.profile.project_name,
            "bytes_processed": response.bytes_processed,
            "bytes_billed": response.bytes_billed,
            "location": response.location,
            "project_id": response.project_id,
            "job_id": response.job_id,
            "slot_ms": response.slot_ms,
            "message": response._message,
        }

    def execute(
        self, sql, auto_begin=False, fetch=None
    ) -> Tuple[BigQueryAdapterResponse, agate.Table]:
        response, table = self.origin_execute(sql, auto_begin, fetch)

        if not hasattr(self, "usages"):
            self.usages = []

            def dump_at_exit():
                print(json.dumps(self.usages))
                pass

            import atexit
            atexit.register(dump_at_exit)

        self.usages.append(self.to_dict(response))

        return response, table


BigQueryConnectionManager.origin_execute = BigQueryConnectionManager.execute
BigQueryConnectionManager.execute = Patched.execute
BigQueryConnectionManager.to_dict = Patched.to_dict

Plugin = HackedAdapterPlugin(
    adapter=dbt_bqcostAdapter,
    credentials=BigQueryCredentials,
    include_path=bigquery.PACKAGE_PATH,
)
