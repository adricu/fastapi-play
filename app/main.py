"""Main application module"""
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app import settings
from app.routers.v1.api import api_router_v1

# TODO: change subdocs URL to be environment aware
tags_metadata = [
    {
        "name": "v1",
        "description": "API version 1, check link on the right",
        "externalDocs": {"description": "sub-docs", "url": "http://127.0.0.1:8000/api/v1/docs"},
    },
]

app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG, openapi_tags=tags_metadata)

api_v1 = FastAPI()

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

api_v1.include_router(api_router_v1)

app.mount(f"{settings.API_PREFIX}/v1", api_v1)


if __name__ == "__main__":  # pragma: no cover
    uvicorn.run(app, host="0.0.0.0", port=8000)
