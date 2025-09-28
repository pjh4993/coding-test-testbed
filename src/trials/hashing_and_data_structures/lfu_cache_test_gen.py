"""LFU Cache Test Generator."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _basic_lfu_cache_test_data():
    """Basic LFU Cache Test Data."""

    return TestCase(
        description="Basic LFU Cache Test",
        expected=[1, -1, 3],
        inputs={
            "size": 2,
            "cmds": [
                "put",
                "put",
                "get",
                "put",
                "get",
                "get",
            ],
            "args": [
                (1, 1),
                (2, 2),
                (1,),
                (3, 3),
                (2,),
                (3,),
            ],
        },
    )


def generate_test_data():
    """Generate test data."""

    TestDataGenerator.generate_test_data(
        [TestDataGeneratorConfig(generator_function=_basic_lfu_cache_test_data)],
        "hashing_and_data_structures/lfu_cache.parquet",
    )


if __name__ == "__main__":
    generate_test_data()
