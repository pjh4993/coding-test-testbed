# -*- coding: utf-8 -*-
"""Test data generator utilities for generating test data."""

import importlib
import json
import logging
from dataclasses import dataclass
from glob import glob
from pathlib import Path
from typing import Callable, List, Optional, Union

import pandas as pd
import yaml
from typing_extensions import Any, Dict

from settings import settings
from utils.sha_utils import SHAHashManager

logger = logging.getLogger(__name__)


@dataclass
class TestCase:
    """Test case."""

    description: str
    inputs: Dict[str, Any]
    expected: Any


@dataclass
class TestDataGeneratorConfig:
    """Test data generator configuration."""

    generator_function: Callable
    score: Optional[int] = None
    time_limit: Optional[int] = None
    memory_limit: Optional[int] = None


class TestDataGenerator:
    """Test data generator utilities for generating test data."""

    @classmethod
    def generate_test_data(
        cls,
        configs: List[TestDataGeneratorConfig],
        path: Union[str, Path],
    ):
        """Generate test data."""

        test_cases: list[TestCase] = []
        for config in configs:
            generated = config.generator_function()

            if not isinstance(generated, list):
                generated = [generated]

            test_cases.extend(generated)

        TestDataGenerator._save_test_data(test_cases, path)

    @staticmethod
    def _save_test_data(test_cases: List[TestCase], path: Union[str, Path]):
        """Save test data."""

        test_data_path = settings.TEST_DATA_DIR / path
        suffix = test_data_path.suffix
        test_data_path.parent.mkdir(parents=True, exist_ok=True)

        match suffix:
            case ".json":
                with open(test_data_path, "w") as f:
                    json.dump(test_cases, f)
            case ".yaml":
                with open(test_data_path, "w") as f:
                    yaml.dump(test_cases, f)
            case ".parquet":
                pd.DataFrame(test_cases).to_parquet(test_data_path)
            case _:
                raise ValueError(f"Unsupported file format: {suffix}")


def generate_test_data_from_generator():
    """Generate test data from a generator."""

    test_data_generators = glob(settings.TEST_DATA_GENERATOR_PATH_PATTERN, recursive=True)
    sha_hash_manager = SHAHashManager()

    for test_data_generator in test_data_generators:
        sha_hash_path = test_data_generator.replace("_test_gen.py", ".sha")
        sha_hash_path = sha_hash_path.replace(
            str(settings.TRIAL_ROOT_DIR), str(settings.TEST_DATA_DIR)
        )

        comparison_result = sha_hash_manager.compare_hash_from_file(
            test_data_generator, sha_hash_path
        )
        if comparison_result.get("match", False):
            logger.info(f"Test data generator {test_data_generator} is up to date.")
            continue
        else:
            logger.info(f"Test data generator {test_data_generator} has changed. Regenerating...")

        module_name = (
            test_data_generator.replace(str(settings.PROJECT_ROOT_DIR), "")
            .lstrip("/")
            .rstrip(".py")
            .replace("/", ".")
        )

        try:
            logger.info(f"Importing module: {module_name}")
            module = importlib.import_module(module_name)
            generator_function = module.generate_test_data

            logger.info(f"Running generator function for {test_data_generator}")
            generator_function()
            logger.info(f"Generator completed for {test_data_generator}")

            logger.info(f"Saving hash for {test_data_generator}")
            sha_hash_manager.generate_and_save_hash(test_data_generator, sha_hash_path)
            logger.info(f"Hash saved for {test_data_generator}")

        except Exception as e:
            logger.error(f"Error during test data generation: {e}")

            raise Exception(f"Test data generation failed: {e}") from e

    return 0
