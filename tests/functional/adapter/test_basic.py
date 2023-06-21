import pytest

from dbt.tests.adapter.basic.test_base import BaseSimpleMaterializations
from dbt.tests.adapter.basic.test_singular_tests import BaseSingularTests
from dbt.tests.adapter.basic.test_singular_tests_ephemeral import (
    BaseSingularTestsEphemeral
)
from dbt.tests.adapter.basic.test_empty import BaseEmpty
from dbt.tests.adapter.basic.test_ephemeral import BaseEphemeral
from dbt.tests.adapter.basic.test_incremental import BaseIncremental
from dbt.tests.adapter.basic.test_generic_tests import BaseGenericTests
from dbt.tests.adapter.basic.test_snapshot_check_cols import BaseSnapshotCheckCols
from dbt.tests.adapter.basic.test_snapshot_timestamp import BaseSnapshotTimestamp
from dbt.tests.adapter.basic.test_adapter_methods import BaseAdapterMethod


class TestSimpleMaterializationsdbt_bqcost(BaseSimpleMaterializations):
    pass


class TestSingularTestsdbt_bqcost(BaseSingularTests):
    pass


class TestSingularTestsEphemeraldbt_bqcost(BaseSingularTestsEphemeral):
    pass


class TestEmptydbt_bqcost(BaseEmpty):
    pass


class TestEphemeraldbt_bqcost(BaseEphemeral):
    pass


class TestIncrementaldbt_bqcost(BaseIncremental):
    pass


class TestGenericTestsdbt_bqcost(BaseGenericTests):
    pass


class TestSnapshotCheckColsdbt_bqcost(BaseSnapshotCheckCols):
    pass


class TestSnapshotTimestampdbt_bqcost(BaseSnapshotTimestamp):
    pass


class TestBaseAdapterMethoddbt_bqcost(BaseAdapterMethod):
    pass
