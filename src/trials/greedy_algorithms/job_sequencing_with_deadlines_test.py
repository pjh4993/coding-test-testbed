"""Job Sequencing with Deadlines Test."""

from trials.greedy_algorithms.job_sequencing_with_deadlines import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="greedy_algorithms/job_sequencing_with_deadlines.parquet",
    input_keys=["jobs"],
    expected_key="expected",
)
def test_job_sequencing_with_deadlines(jobs, expected, description):
    """Test job sequencing with deadlines."""

    run_and_assert(solution, (jobs,), expected, description)
