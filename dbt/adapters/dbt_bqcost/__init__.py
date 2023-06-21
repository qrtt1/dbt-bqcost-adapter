from dbt.adapters.base import AdapterPlugin
from dbt.adapters.bigquery import BigQueryCredentials
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
            FACTORY.plugins["bigquerycost"] = FACTORY.plugins["bigquery"]
        return super().__getattribute__(item)


Plugin = HackedAdapterPlugin(
    adapter=dbt_bqcostAdapter,
    credentials=BigQueryCredentials,
    include_path=bigquery.PACKAGE_PATH,
)
