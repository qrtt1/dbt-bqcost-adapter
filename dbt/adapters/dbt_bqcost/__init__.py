from dbt.adapters.dbt_bqcost.connections import dbt_bqcostConnectionManager # noqa
from dbt.adapters.dbt_bqcost.connections import dbt_bqcostCredentials
from dbt.adapters.dbt_bqcost.impl import dbt_bqcostAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import dbt_bqcost


Plugin = AdapterPlugin(
    adapter=dbt_bqcostAdapter,
    credentials=dbt_bqcostCredentials,
    include_path=dbt_bqcost.PACKAGE_PATH
    )
