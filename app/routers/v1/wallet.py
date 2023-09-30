"""Wallet api v1"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.utils.common import validate_address
from app.utils.contract import get_acr_balance, get_nft_balance

router = APIRouter()


class BalanceResponse(BaseModel):
    """Balance response model"""

    erc20: str
    erc721: int


@router.get("/balance/{address}", response_model=BalanceResponse)
async def balance(address: str) -> BalanceResponse:
    """Balance endpoint"""
    if not validate_address(address):
        raise HTTPException(status_code=400, detail=f"{address} is not a valid address")
    return BalanceResponse(erc20=f"{get_acr_balance(address):.2f}", erc721=get_nft_balance(address))
