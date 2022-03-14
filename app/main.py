"""Main application module"""
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from app import settings

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")


class MainResponse(BaseModel):
    """Main response model"""

    message: str


class BalanceResponse(BaseModel):
    """Balance response model"""

    erc20: str
    erc721: int


@app.get("/", response_model=MainResponse)
async def root():
    """Root endpoint"""
    return {"message": "Hello World"}


@app.get("/balance/{address}", response_model=BalanceResponse)
async def balance():
    """Balance endpoint"""
    return {"erc20": 1, "erc721": 2}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
