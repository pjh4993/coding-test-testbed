"""Test data loader utilities for managing test cases in external files."""

import json
import logging
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, List, Union

import numpy as np
import pytest

from settings import settings

logger = logging.getLogger(__name__)


class TestDataLoader:
    """Test data loader utilities for managing test cases in external files."""

    INTERESTED_FILE_EXTENSIONS = (".json", ".yaml", ".parquet")

    @staticmethod
    def _load_test_cases_from_json(file_path: Union[str, Path]) -> List[Dict[str, Any]]:
        """Load test cases from a JSON file.

        Expected JSON format:
        {
            "test_cases": [
                {
                    "description": "Test case description",
                    "inputs": {...},
                    "expected": {...}
                }
            ]
        }

        Args:
            file_path: Path to the JSON file containing test cases

        Returns:
            List of test case dictionaries
        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"Test data file not found: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if "test_cases" not in data:
            raise ValueError("JSON file must contain 'test_cases' key")

        return data["test_cases"]

    @staticmethod
    def _load_test_cases_from_yaml(file_path: Union[str, Path]) -> List[Dict[str, Any]]:
        """Load test cases from a YAML file.

        Args:
            file_path: Path to the YAML file containing test cases

        Returns:
            List of test case dictionaries
        """
        try:
            import yaml
        except ImportError:
            raise ImportError(
                "PyYAML is required for YAML support. Install with: pip install pyyaml"
            )

        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"Test data file not found: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        if "test_cases" not in data:
            raise ValueError("YAML file must contain 'test_cases' key")

        return data["test_cases"]

    @staticmethod
    def _load_test_cases_from_parquet(
        file_path: Union[str, Path],
    ) -> List[Dict[str, Any]]:
        """Load test cases from a Parquet file.

        Expected Parquet format with columns:
        - description: Test case description
        - input_*: Input parameters (e.g., input_nums, input_k, input_target)
        - expected: Expected result

        Args:
            file_path: Path to the Parquet file containing test cases

        Returns:
            List of test case dictionaries
        """
        try:
            import pandas as pd
        except ImportError:
            raise ImportError(
                "pandas is required for Parquet support. Install with: pip install pandas pyarrow"
            )

        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"Test data file not found: {file_path}")

        # Read the parquet file
        df = pd.read_parquet(file_path)

        # Check if any of the columns are numpy and convert to list
        for col in df.columns:
            if isinstance(df[col].iloc[0], np.ndarray):
                df[col] = df[col].apply(lambda x: x.tolist())

        # Convert DataFrame to list of dictionaries
        test_cases = []
        for _, row in df.iterrows():
            case = {}

            # Add description if present
            if "description" in df.columns:
                case["description"] = row["description"]

            # Add expected result
            if "expected" in df.columns:
                case["expected"] = row["expected"]

            # Add input if exists
            if "inputs" in df.columns:
                case["inputs"] = row["inputs"]

            test_cases.append(case)

        return test_cases

    @staticmethod
    def _parametrize_from_file(
        file_path: Union[str, Path],
        input_keys: List[str],
        expected_key: str = "expected",
        description_key: str = "description",
    ) -> pytest.MarkDecorator:
        """Create a pytest parametrize decorator from a test data file.

        Args:
            file_path: Path to the test data file (JSON, YAML, or Parquet)
            input_keys: List of keys to extract as input parameters
            expected_key: Key for the expected result
            description_key: Key for test case description (optional)

        Returns:
            pytest.mark.parametrize decorator
        """
        file_path = Path(file_path)

        if file_path.suffix.lower() == ".json":
            test_cases = TestDataLoader._load_test_cases_from_json(file_path)
        elif file_path.suffix.lower() in [".yml", ".yaml"]:
            test_cases = TestDataLoader._load_test_cases_from_yaml(file_path)
        elif file_path.suffix.lower() == ".parquet":
            test_cases = TestDataLoader._load_test_cases_from_parquet(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_path.suffix}")

        # Extract parameters for pytest
        params = []
        for case in test_cases:
            param = []

            # Add input parameters in order
            for key in input_keys:
                if key not in case.get("inputs", {}):
                    raise KeyError(f"Input key '{key}' not found in test case")
                param.append(deepcopy(case["inputs"][key]))

            # Add expected result
            if expected_key not in case:
                raise KeyError(f"Expected key '{expected_key}' not found in test case")
            param.append(deepcopy(case[expected_key]))

            # Add description if available
            if description_key in case:
                param.append(deepcopy(case[description_key]))

            params.append(tuple(param))

        # Create parameter names
        param_names = input_keys + [expected_key]
        if description_key in test_cases[0] if test_cases else False:
            param_names.append(description_key)

        return pytest.mark.parametrize(",".join(param_names), params)

    @classmethod
    def parametrize(
        cls,
        path_or_fixture: Union[str, Path],
        input_keys: List[str],
        expected_key: str = "expected",
        description_key: str = "description",
    ) -> pytest.MarkDecorator:
        """Create a pytest parametrize decorator from a test data file or fixture.

        Args:
            path_or_fixture: Path to the test data file or pytest fixture
            input_keys: List of keys to extract as input parameters
            expected_key: Key for the expected result
            description_key: Key for test case description (optional)

        Returns:
            pytest.mark.parametrize decorator
        """

        logger.debug(f"Creating pytest parametrize decorator from {path_or_fixture}")

        # If the path_or_fixture is a string and ends with .json, .yaml, or .parquet, load the test cases from the file
        if cls._is_file_path(path_or_fixture):
            file_path = settings.TEST_DATA_DIR / path_or_fixture
            return TestDataLoader._parametrize_from_file(
                file_path=file_path,
                input_keys=input_keys,
                expected_key=expected_key,
                description_key=description_key,
            )
        # If the path_or_fixture is a string and
        elif cls._is_dir_path(path_or_fixture):
            raise NotImplementedError("Directory path is not supported yet")
        # If the path_or_fixture is a pytest fixture, return the fixture
        elif cls._is_fixture(path_or_fixture):
            return pytest.mark.parametrize(path_or_fixture, input_keys)

        raise ValueError(
            f"Invalid path_or_fixture: {path_or_fixture},"
            "must be a file path, directory path, or pytest fixture"
        )

    @classmethod
    def _is_file_path(cls, path_or_fixture: Union[str, Path]) -> bool:
        """Check if the path_or_fixture is a file path."""

        return isinstance(path_or_fixture, str) and path_or_fixture.endswith(
            cls.INTERESTED_FILE_EXTENSIONS
        )

    @classmethod
    def _is_dir_path(cls, path_or_fixture: Union[str, Path]) -> bool:
        """Check if the path_or_fixture is a directory path."""

        return isinstance(path_or_fixture, str) and Path(path_or_fixture).is_dir()

    @classmethod
    def _is_fixture(cls, path_or_fixture: Union[str, Path]) -> bool:
        """Check if the path_or_fixture is a pytest fixture."""

        return isinstance(path_or_fixture, pytest.fixture)
