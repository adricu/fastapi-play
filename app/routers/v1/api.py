"""API v1 router"""
from fastapi import APIRouter

from app.routers.v1 import wallet

api_router_v1 = APIRouter()
api_router_v1.include_router(wallet.router, prefix="/wallet", tags=["wallet"])
