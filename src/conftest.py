# -*- coding: utf-8 -*-
"""Pytest configuration and plugins."""

import os

from utils.data_generator import generate_test_data_from_generator


def pytest_configure(config):
    """Configure pytest and generate test data before running tests."""
    # Check if test data generation should be skipped
    if os.getenv("SKIP_TEST_DATA_GENERATION"):
        print("\n⏭️  Skipping test data generation (SKIP_TEST_DATA_GENERATION=1)")
        return

    print("\n🔄 Generating test data...")

    try:
        # Run testbed generate-test-data command
        # Using shell=False for security (no shell injection)
        result = generate_test_data_from_generator()

        if result == 0:
            print("✅ Test data generated successfully")
        else:
            print("⚠️  Warning: Test data generation had issues:")

    except Exception as e:
        print(f"⚠️  Warning: Could not generate test data: {e}")
        print("   Tests may fail if test data is missing")


def pytest_sessionstart(session):
    """Called after the Session object has been created."""
    print("\n🚀 Starting test session with generated data")


def pytest_sessionfinish(session, exitstatus):
    """Called after whole test run finished."""
    if exitstatus == 0:
        print("\n✅ All tests passed!")
    else:
        print(f"\n❌ Tests failed with exit status: {exitstatus}")
