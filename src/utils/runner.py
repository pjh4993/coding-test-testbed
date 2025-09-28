"""Utility functions."""

import logging
from typing import Any, Callable, Tuple

logger = logging.getLogger(__name__)


def run_and_assert(
    solution: Callable, in_args: Tuple, expected: Any, description: str = ""
):
    """Assert and print the expected and actual values."""

    actual = "Not run"

    try:
        logger.debug("--------------------------------")
        logger.debug(f"Running test: {description}")
        actual = solution(*in_args)
        assert expected == actual
    except AssertionError as ase:
        logger.debug("AssertionError: %s", ase, exc_info=True)
        raise ase
    except Exception as e:
        logger.debug("Exception: %s", e, exc_info=True)
        raise e
    finally:
        logger.debug(f"Expected: {expected}, Actual: {actual}")
        logger.debug("--------------------------------")
