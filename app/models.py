"""Common models."""
from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Status response model"""

    status: str
