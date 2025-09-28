"""Job Sequencing with Deadlines Test Generator."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _basic_job_sequencing():
    """Common example; expected is max profit only."""
    # Optimal: jobs [3,1] with profit 40 + 20 = 60
    return TestCase(
        description="Basic job sequencing",
        expected=60,
        inputs={
            "jobs": [
                (1, 4, 20),  # (id, deadline, profit)
                (2, 1, 10),
                (3, 1, 40),
                (4, 1, 30),
            ]
        },
    )


def _spread_deadlines():
    """Jobs with spread deadlines; greedy by profit then latest slot."""
    # One optimal schedule yields profit 150 (e.g., pick 100@d3, 50@d2)
    return TestCase(
        description="Spread deadlines",
        expected=180,
        inputs={
            "jobs": [
                (1, 2, 50),
                (2, 1, 10),
                (3, 2, 20),
                (4, 3, 100),
                (5, 1, 30),
            ]
        },
    )


def _tight_deadlines_many_jobs():
    """Many jobs but tight slots; greedy should pick highest profits fitting in 2 slots."""
    # Deadlines <= 2, best is to pick two highest profits that can schedule: 70 and 60 -> 130
    return TestCase(
        description="Tight deadlines with many jobs",
        expected=130,
        inputs={
            "jobs": [
                (1, 1, 20),
                (2, 2, 60),
                (3, 2, 70),
                (4, 1, 30),
                (5, 2, 10),
            ]
        },
    )


def _all_same_deadline():
    """All jobs have same deadline; only one job can be done."""
    # All deadline=1; pick highest profit=90
    return TestCase(
        description="All same deadline",
        expected=90,
        inputs={
            "jobs": [
                (1, 1, 20),
                (2, 1, 50),
                (3, 1, 40),
                (4, 1, 90),
            ]
        },
    )


def generate_test_data():
    """Generate job sequencing test data."""
    TestDataGenerator.generate_test_data(
        [
            TestDataGeneratorConfig(generator_function=_basic_job_sequencing),
            TestDataGeneratorConfig(generator_function=_spread_deadlines),
            TestDataGeneratorConfig(generator_function=_tight_deadlines_many_jobs),
            TestDataGeneratorConfig(generator_function=_all_same_deadline),
        ],
        "greedy_algorithms/job_sequencing_with_deadlines.parquet",
    )


if __name__ == "__main__":
    generate_test_data()
