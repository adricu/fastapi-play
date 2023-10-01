"""Logging configurations."""
import logging.config
from typing import Any

from envyaml import EnvYAML


def get_log_config(config: EnvYAML) -> dict[str, Any]:
    """Return configuration for logging."""
    formatter = config["logging.formatter"]
    handler = config["logging.handler"]
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {
                "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
                "fmt": "%(asctime)s %(filename)s %(funcName)s %(levelname)s %(lineno)d %(message)s "
                "%(module)s %(name)s %(pathname)s %(process)d %(thread)d",
                "rename_fields": {
                    "levelname": "level",
                },
                "timestamp": True,
            },
            "verbose": {
                "format": "%(asctime)s [%(levelname)s] %(name)s %(process)d %(thread)d: %(message)s",
            },
            "standard": {
                "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            },
            "simple": {
                "format": "[%(levelname)s] %(message)s",
            },
        },
        "handlers": {
            "stdout": {
                "level": "NOTSET",
                "class": "logging.StreamHandler",
                "formatter": formatter,
                "stream": "ext://sys.stdout",
            },
            "file": {
                "level": "NOTSET",
                "class": "logging.FileHandler",
                "formatter": formatter,
                "filename": "app.log",
                "delay": True,
            },
        },
        "root": {
            "handlers": [handler],
            "level": config["logging.logger.root"],
        },
        "loggers": {
            "app": {
                "handlers": [handler],
                "level": config["logging.logger.app"],
                "propagate": False,
            },
            "uvicorn": {
                "handlers": [handler],
                "level": config["logging.logger.uvicorn"],
                "propagate": False,
            },
        },
    }


def configure_logging(config: EnvYAML) -> None:
    """Setup python logging."""
    log_config = get_log_config(config)
    logging.config.dictConfig(log_config)
