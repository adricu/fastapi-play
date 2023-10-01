"""Models v1."""
from pydantic import BaseModel


class BalanceResponse(BaseModel):
    """Balance response model"""

    erc20: str
    erc721: int
