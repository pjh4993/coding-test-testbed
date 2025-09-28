# -*- coding: utf-8 -*-
"""Course Schedule Problem Test."""

from trials.graph_algorithms.course_schedule import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="graph_algorithms/course_schedule.parquet",
    input_keys=["n", "prerequisites"],
    expected_key="expected",
)
def test_course_schedule(n, prerequisites, expected, description):
    """Test course schedule."""

    run_and_assert(solution, (n, prerequisites), expected, description)
