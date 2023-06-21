
from dbt.adapters.sql import SQLAdapter as adapter_cls

from dbt.adapters.dbt_bqcost import dbt_bqcostConnectionManager



class dbt_bqcostAdapter(adapter_cls):
    """
    Controls actual implmentation of adapter, and ability to override certain methods.
    """

    ConnectionManager = dbt_bqcostConnectionManager

    @classmethod
    def date_function(cls):
        """
        Returns canonical date func
        """
        return "datenow()"

 # may require more build out to make more user friendly to confer with team and community.
