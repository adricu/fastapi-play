"""Main application module"""
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class MainResponse(BaseModel):
    """Main response model"""

    message: str


@app.get("/", response_model=MainResponse)
async def root():
    """Root endpoint"""
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
