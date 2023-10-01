"""Wallet api v1"""
from envyaml import EnvYAML
from fastapi import APIRouter, FastAPI, HTTPException

from app.routers.v1.models import BalanceResponse
from app.utils.contract import get_acr_balance, get_nft_balance, validate_address


def get_wallet_router(config: EnvYAML) -> FastAPI:
    """Return wallet router."""
    router = APIRouter()

    @router.get("/balance/{address}", response_model=BalanceResponse)
    async def balance(address: str) -> BalanceResponse:
        """Balance endpoint."""
        if not validate_address(address):
            raise HTTPException(status_code=400, detail=f"{address} is not a valid address")
        blockchain_config = config["blockchain"]
        return BalanceResponse(
            erc20=f"{get_acr_balance(blockchain_config, address):.2f}",
            erc721=get_nft_balance(blockchain_config, address),
        )

    return router
