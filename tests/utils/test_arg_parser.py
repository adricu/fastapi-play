"""Arg parser tests."""
import pytest

from app.utils.arg_parser import parse_api_args


def test_parse_api_args() -> None:
    """Parse api args test."""
    parse_api_args(["staging"])
    with pytest.raises(SystemExit):
        parse_api_args(["non_exist_env"])
