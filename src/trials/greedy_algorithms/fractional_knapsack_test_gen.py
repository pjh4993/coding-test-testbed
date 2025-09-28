"""Fractional Knapsack Test Generator."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _classic_fractional_knapsack():
    """Classic example where answer is a neat float."""
    return TestCase(
        description="Classic fractional knapsack",
        expected=240.0,
        inputs={
            "capacity": 50,
            "values": [60, 100, 120],
            "weights": [10, 20, 30],
        },
    )


def _capacity_zero():
    """Edge: zero capacity."""
    return TestCase(
        description="Zero capacity",
        expected=0.0,
        inputs={
            "capacity": 0,
            "values": [10, 20, 30],
            "weights": [5, 10, 20],
        },
    )


def _take_all_items():
    """Capacity large enough to take everything fully."""
    return TestCase(
        description="Take all items",
        expected=10 + 40 + 15,  # = 65.0
        inputs={
            "capacity": 1000,
            "values": [10, 40, 15],
            "weights": [5, 20, 10],
        },
    )


def _tie_on_ratio():
    """Two items with same ratio; order shouldn't affect result."""
    # values/weights -> [ (20/5)=4, (8/2)=4, (15/5)=3 ]
    # capacity 6: take 2 units of any 4-ratio item (8) + 4/5 of the 20-valued item? Let's compute:
    # Greedy with equal highest ratios: pick (20,5) -> take 5 => value 20, rem cap=1; then (8,2) -> take 1 => 4
    # total = 24.0. Any correct tie handling should reach 24.0.
    return TestCase(
        description="Tie on value-to-weight ratio",
        expected=24.0,
        inputs={
            "capacity": 6,
            "values": [20, 8, 15],
            "weights": [5, 2, 5],
        },
    )


def generate_test_data():
    """Generate fractional knapsack test data."""
    TestDataGenerator.generate_test_data(
        [
            TestDataGeneratorConfig(generator_function=_classic_fractional_knapsack),
            TestDataGeneratorConfig(generator_function=_capacity_zero),
            TestDataGeneratorConfig(generator_function=_take_all_items),
            TestDataGeneratorConfig(generator_function=_tie_on_ratio),
        ],
        "greedy_algorithms/fractional_knapsack.parquet",
    )


if __name__ == "__main__":
    generate_test_data()
