"""Common utils."""
from enum import Enum
from pathlib import Path

from envyaml import EnvYAML

BASE_DIR = Path(__file__).resolve().parent.parent.parent
REQUESTS_TIMEOUT = (3.05, 27)


class Environment(str, Enum):
    """Enviornment possibilities."""

    LOCAL = "local"
    TEST = "test"
    STAGING = "staging"
    PRODUCTION = "production"


ENVIRONMENTS = [environment.value for environment in Environment]


def load_config(environment: Environment) -> EnvYAML:
    """Load and return app confiuration"""
    config_file_path = f"config/{environment}.yaml"
    if not Path(config_file_path).is_file():
        raise ValueError(
            f"Unable to find configuration file: {config_file_path}."
        )  # pragma: no cover
    return EnvYAML(config_file_path)
