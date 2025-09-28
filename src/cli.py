"""CLI for the project."""

import logging
import sys

import click

from utils.data_generator import generate_test_data_from_generator


def setup_logger(level: str = "INFO", verbose: bool = False) -> logging.Logger:
    """
    Set up logger for CLI with stdio output.

    Args:
        level: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        verbose: If True, use DEBUG level regardless of level parameter

    Returns:
        Configured logger
    """
    # Create logger
    logger = logging.getLogger()

    # Clear any existing handlers
    logger.handlers.clear()

    # Set level
    if verbose:
        log_level = logging.DEBUG
    else:
        log_level = getattr(logging, level.upper(), logging.INFO)

    logger.setLevel(log_level)

    # Create console handler for stdio
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)

    # Create formatter
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)8s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    console_handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(console_handler)

    # Prevent propagation to root logger
    logger.propagate = False

    return logger


def get_logger(name: str = None) -> logging.Logger:
    """
    Get a logger instance for use throughout the application.

    Args:
        name: Logger name (defaults to calling module)

    Returns:
        Logger instance
    """
    return logging.getLogger(name)


@click.group()
@click.option(
    "--log-level",
    type=click.Choice(
        ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], case_sensitive=False
    ),
    default="INFO",
    help="Set the logging level",
)
@click.option(
    "--verbose", "-v", is_flag=True, help="Enable verbose logging (DEBUG level)"
)
@click.pass_context
def cli(ctx, log_level, verbose):
    """CLI for the project."""
    # Setup logger
    logger = setup_logger(level=log_level, verbose=verbose)

    # Store logger in context for use in commands
    ctx.ensure_object(dict)
    ctx.obj["logger"] = logger

    logger.info(f"CLI started with log level: {log_level if not verbose else 'DEBUG'}")


@cli.command()
@click.pass_context
def generate_test_data(ctx):
    """Generate test data."""
    logger = ctx.obj["logger"]
    logger.info("Starting test data generation...")

    try:
        generate_test_data_from_generator()
        logger.info("Test data generation completed successfully")
    except Exception as e:
        logger.error(f"Error during test data generation: {e}")
        raise click.ClickException(f"Test data generation failed: {e}")


if __name__ == "__main__":
    cli()
