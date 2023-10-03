"""Module with authentication logic."""
import secrets
from typing import Annotated, Callable

from envyaml import EnvYAML
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials


def get_current_username_wrapper(config: EnvYAML) -> Callable:
    """Get current username dependency wrapper."""
    users = {
        "public": str(config["api"]["auth"]["public_password"]).encode("utf8"),
        "secure": str(config["api"]["auth"]["secure_password"]).encode("utf8"),
    }
    security = HTTPBasic()

    def get_current_username(
        credentials: Annotated[HTTPBasicCredentials, Depends(security)]
    ) -> str:
        for user, password in users.items():
            current_username_bytes = credentials.username.encode("utf8")
            is_correct_username = secrets.compare_digest(
                current_username_bytes, user.encode("utf8")
            )
            current_password_bytes = credentials.password.encode("utf8")
            is_correct_password = secrets.compare_digest(
                current_password_bytes, password
            )
            if is_correct_username and is_correct_password:
                return credentials.username
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return get_current_username
