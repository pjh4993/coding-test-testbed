# -*- coding: utf-8 -*-
"""Alternative pytest plugin for test data generation."""

import subprocess
import sys
from pathlib import Path

import pytest


@pytest.fixture(scope="session", autouse=True)
def generate_test_data():
    """Generate test data before running any tests."""
    print("\n🔄 Auto-generating test data...")

    try:
        result = subprocess.run(  # noqa: S603
            [sys.executable, "-m", "testbed", "generate-test-data"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent,
        )

        if result.returncode == 0:
            print("✅ Test data generated successfully")
            yield
        else:
            print("⚠️  Warning: Test data generation failed:")
            print(f"   stdout: {result.stdout}")
            print(f"   stderr: {result.stderr}")
            yield

    except Exception as e:
        print(f"⚠️  Warning: Could not generate test data: {e}")
        yield


# Alternative: Use this if you want to generate data only for specific test modules
@pytest.fixture(scope="module", autouse=True)
def generate_test_data_per_module():
    """Generate test data for each test module."""
    # This runs once per test module
    pass
