"""App main controller."""
from envyaml import EnvYAML
from fastapi import FastAPI

from app.exception_handlers import register_exception_handlers
from app.models import HealthResponse
from app.routers.v1.controller import get_api_v1


def create_api(config: EnvYAML) -> FastAPI:
    """Create main FastAPI application."""
    tags_metadata = [
        {
            "name": "v1",
            "description": "API version 1, check link on the right",
            "externalDocs": {"description": "sub-docs", "url": "http://127.0.0.1:8000/v1/docs"},
        },
    ]
    api = FastAPI(title=config["api"]["title"], openapi_tags=tags_metadata)
    register_exception_handlers(api)

    @api.get("/healthz", response_model=HealthResponse)
    def healthz() -> HealthResponse:
        return HealthResponse(status="ok")

    api.mount("/v1", get_api_v1(config))
    return api
