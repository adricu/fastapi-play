"""Exception handlers."""
import logging

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

LOGGER = logging.getLogger(__name__)


def register_exception_handlers(api: FastAPI) -> None:
    """Register exception handlers."""

    @api.exception_handler(Exception)
    def unhandled_exception(_: Request, exc: Exception) -> JSONResponse:
        LOGGER.exception("API unhandled exception")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error_message": f"API unhandled exception: {str(exc)}"},
        )
