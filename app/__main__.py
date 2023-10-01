"""Main Entrypoint module."""
import uvicorn

from app.utils.arg_parser import parse_api_args
from app.utils.common import load_config
from app.utils.logging.config import configure_logging, get_log_config


def main() -> None:
    """App entrypoint."""
    environment = parse_api_args()
    config = load_config(environment)
    configure_logging(config)
    api_config = config["api"]

    uvicorn.run(
        "app.api:api",
        host=api_config["host"],
        port=api_config["port"],
        log_config=get_log_config(config),
        access_log=api_config["access_log"],
        workers=api_config["workers"],
        reload=api_config["reload"],
    )


if __name__ == "__main__":  # pragma: no cover
    main()
