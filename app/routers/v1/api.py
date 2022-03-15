"""API v1 router"""
from fastapi import APIRouter

from app.routers.v1 import wallet

api_router = APIRouter()
api_router.include_router(wallet.router, prefix="/wallet", tags=["wallet"])
