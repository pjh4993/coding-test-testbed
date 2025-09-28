"""Settings."""

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings

WORKSPACE_DIR = Path(__file__).parent.parent.absolute()


class Settings(BaseSettings):
    """Settings."""

    PROJECT_ROOT_DIR: Path = Field(default_factory=lambda: WORKSPACE_DIR / "src")
    TRIAL_ROOT_DIR: Path = Field(
        default_factory=lambda: WORKSPACE_DIR / "src" / "trials"
    )
    TEST_DATA_DIR: Path = Field(default_factory=lambda: WORKSPACE_DIR / "data")
    TEST_DATA_GENERATOR_PATH_PATTERN: str = Field(
        default_factory=lambda: str(WORKSPACE_DIR / "**/*_test_gen.py")
    )


settings = Settings()
