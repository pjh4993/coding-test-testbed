"""Group Anagrams Test Generator."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _basic_group_anagrams_test_data():
    """Generate basic group anagrams test data."""

    return TestCase(
        description="Basic group anagrams test",
        expected=[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        inputs={
            "strs": ["eat", "tea", "tan", "ate", "nat", "bat"],
        },
    )


def _empty_list_test_data():
    """Test case for empty input list."""
    return TestCase(
        description="Empty list test",
        expected=[],
        inputs={
            "strs": [],
        },
    )


def _single_string_test_data():
    """Test case for single string."""
    return TestCase(
        description="Single string test",
        expected=[["a"]],
        inputs={
            "strs": ["a"],
        },
    )


def _no_anagrams_test_data():
    """Test case where no strings are anagrams of each other."""
    return TestCase(
        description="No anagrams test",
        expected=[["abc"], ["def"], ["ghi"]],
        inputs={
            "strs": ["abc", "def", "ghi"],
        },
    )


def _all_same_anagrams_test_data():
    """Test case where all strings are anagrams of each other."""
    return TestCase(
        description="All same anagrams test",
        expected=[["listen", "silent", "enlist"]],
        inputs={
            "strs": ["listen", "silent", "enlist"],
        },
    )


def _single_character_strings_test_data():
    """Test case with single character strings."""
    return TestCase(
        description="Single character strings test",
        expected=[["a", "a"], ["b"], ["c", "c"]],
        inputs={
            "strs": ["a", "b", "c", "a", "c"],
        },
    )


def _case_sensitive_test_data():
    """Test case with case sensitive strings (should not group different cases)."""
    return TestCase(
        description="Case sensitive test",
        expected=[["abc", "bca"], ["ABC"]],
        inputs={
            "strs": ["abc", "ABC", "bca"],
        },
    )


def _duplicate_strings_test_data():
    """Test case with duplicate strings."""
    return TestCase(
        description="Duplicate strings test",
        expected=[["eat", "eat", "tea"], ["bat"]],
        inputs={
            "strs": ["eat", "eat", "tea", "bat"],
        },
    )


def _long_strings_test_data():
    """Test case with longer strings."""
    return TestCase(
        description="Long strings test",
        expected=[["abcdefghij", "jihgfedcba"], ["xyz", "zyx"]],
        inputs={
            "strs": ["abcdefghij", "xyz", "jihgfedcba", "zyx"],
        },
    )


def _special_characters_test_data():
    """Test case with special characters."""
    return TestCase(
        description="Special characters test",
        expected=[["a!@#", "#@!a"], ["b$%", "%$b"]],
        inputs={
            "strs": ["a!@#", "b$%", "#@!a", "%$b"],
        },
    )


def _numbers_in_strings_test_data():
    """Test case with numbers in strings."""
    return TestCase(
        description="Numbers in strings test",
        expected=[["a1b2", "b2a1"], ["c3d4"]],
        inputs={
            "strs": ["a1b2", "c3d4", "b2a1"],
        },
    )


def _mixed_lengths_test_data():
    """Test case with strings of different lengths."""
    return TestCase(
        description="Mixed lengths test",
        expected=[["a"], ["ab", "ba"], ["abc", "bca", "cab"]],
        inputs={
            "strs": ["a", "ab", "ba", "abc", "bca", "cab"],
        },
    )


def _large_input_test_data():
    """Test case with larger input set."""
    return TestCase(
        description="Large input test",
        expected=[["act", "cat", "tac"], ["dog", "god"], ["rat"], ["bat", "tab"]],
        inputs={
            "strs": ["act", "cat", "dog", "rat", "bat", "tac", "god", "tab"],
        },
    )


def generate_test_data():
    """Generate test data."""

    configs = [
        TestDataGeneratorConfig(generator_function=_basic_group_anagrams_test_data),
        TestDataGeneratorConfig(generator_function=_empty_list_test_data),
        TestDataGeneratorConfig(generator_function=_single_string_test_data),
        TestDataGeneratorConfig(generator_function=_no_anagrams_test_data),
        TestDataGeneratorConfig(generator_function=_all_same_anagrams_test_data),
        TestDataGeneratorConfig(generator_function=_single_character_strings_test_data),
        TestDataGeneratorConfig(generator_function=_case_sensitive_test_data),
        TestDataGeneratorConfig(generator_function=_duplicate_strings_test_data),
        TestDataGeneratorConfig(generator_function=_long_strings_test_data),
        TestDataGeneratorConfig(generator_function=_special_characters_test_data),
        TestDataGeneratorConfig(generator_function=_numbers_in_strings_test_data),
        TestDataGeneratorConfig(generator_function=_mixed_lengths_test_data),
        TestDataGeneratorConfig(generator_function=_large_input_test_data),
    ]

    TestDataGenerator.generate_test_data(
        configs, "hashing_and_data_structures/group_anagrams.parquet"
    )


if __name__ == "__main__":
    generate_test_data()
