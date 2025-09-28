# -*- coding: utf-8 -*-
"""Course Schedule Problem Test Generator."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _valid_schedule_test():
    """Valid schedule test case."""
    return TestCase(
        description="Valid schedule",
        expected=True,
        inputs={
            "n": 4,
            "prerequisites": [(1, 0), (2, 1), (3, 2)],
        },
    )


def _cycle_detected_test():
    """Cycle detected test case."""
    return TestCase(
        description="Cycle detected",
        expected=False,
        inputs={
            "n": 2,
            "prerequisites": [(0, 1), (1, 0)],
        },
    )


def _no_prerequisites_test():
    """No prerequisites test case."""
    return TestCase(
        description="No prerequisites",
        expected=True,
        inputs={
            "n": 3,
            "prerequisites": [],
        },
    )


def _single_course_test():
    """Single course test case."""
    return TestCase(
        description="Single course",
        expected=True,
        inputs={
            "n": 1,
            "prerequisites": [],
        },
    )


def _complex_cycle_test():
    """Complex cycle test case."""
    return TestCase(
        description="Complex cycle",
        expected=False,
        inputs={
            "n": 3,
            "prerequisites": [(0, 1), (1, 2), (2, 0)],
        },
    )


def generate_test_data():
    """Generate course schedule test data."""
    TestDataGenerator.generate_test_data(
        [
            TestDataGeneratorConfig(generator_function=_valid_schedule_test),
            TestDataGeneratorConfig(generator_function=_cycle_detected_test),
            TestDataGeneratorConfig(generator_function=_no_prerequisites_test),
            TestDataGeneratorConfig(generator_function=_single_course_test),
            TestDataGeneratorConfig(generator_function=_complex_cycle_test),
        ],
        "graph_algorithms/course_schedule.parquet",
    )


if __name__ == "__main__":
    generate_test_data()
