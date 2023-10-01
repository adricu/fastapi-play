"""API v1 router"""
from envyaml import EnvYAML
from fastapi import FastAPI

from app.routers.v1.wallet import get_wallet_router


def get_api_v1(config: EnvYAML) -> FastAPI:
    """Return v1 app."""
    api_v1 = FastAPI(title=f"v1 {config['api']['title']}")
    api_v1.include_router(get_wallet_router(config), prefix="/wallet", tags=["wallet"])
    return api_v1
