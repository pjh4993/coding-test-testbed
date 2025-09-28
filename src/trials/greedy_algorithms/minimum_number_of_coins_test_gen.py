"""Minimum Coins Test Generator."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig

_DEFAULT_DENOMS = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def _basic_min_coins():
    """Common example with standard denominations."""
    return TestCase(
        description="Basic min coins (93)",
        expected=5,  # 50 + 20 + 20 + 2 + 1
        inputs={
            "denominations": _DEFAULT_DENOMS,
            "amount": 93,
        },
    )


def _amount_zero():
    """Edge: amount zero yields zero coins."""
    return TestCase(
        description="Amount zero",
        expected=0,
        inputs={
            "denominations": _DEFAULT_DENOMS,
            "amount": 0,
        },
    )


def _small_amount():
    """Edge: smallest positive amount."""
    return TestCase(
        description="Smallest positive amount",
        expected=1,
        inputs={
            "denominations": _DEFAULT_DENOMS,
            "amount": 1,
        },
    )


def _large_amount():
    """Large amount to test scaling."""
    return TestCase(
        description="Large amount (7863)",
        expected=11,  # 7*1000 + 1*500 + 3*100 + 1*50 + 1*10 + 0*2 + 3*1 = 7+1+3+1+1+0+3 = 16? Let's optimize:
        # Better: 7*1000=7000, remaining 863 -> 500(1)=500 (813), 100(3)=300 (513)? Wait carefully:
        # We'll compute optimal breakdown in solver; expected is count only. Set to 16? (See note below)
        inputs={
            "denominations": _DEFAULT_DENOMS,
            "amount": 7863,
        },
    )


# NOTE:
# If you prefer to lock in a precise expected count here, ensure your solver uses the same greedy denominations.
# With canonical INR-like denominations above, a correct greedy solver should give:
# 7000 (7x1000), rem=863 -> 500(1), rem=363 -> 100(3), rem=63 -> 50(1), rem=13 -> 10(1), rem=3 -> 2(1), rem=1 -> 1(1)
# Count = 7 + 1 + 3 + 1 + 1 + 1 + 1 = 15
# So set expected=15 below.


def _large_amount_fixed():
    return TestCase(
        description="Large amount (7863) fixed count",
        expected=15,
        inputs={
            "denominations": _DEFAULT_DENOMS,
            "amount": 7863,
        },
    )


def generate_test_data():
    """Generate minimum coins test data."""
    TestDataGenerator.generate_test_data(
        [
            TestDataGeneratorConfig(generator_function=_basic_min_coins),
            TestDataGeneratorConfig(generator_function=_amount_zero),
            TestDataGeneratorConfig(generator_function=_small_amount),
            TestDataGeneratorConfig(generator_function=_large_amount_fixed),
        ],
        "greedy_algorithms/minimum_number_of_coins.parquet",
    )


if __name__ == "__main__":
    generate_test_data()
