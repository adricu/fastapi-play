"""API Creation."""
from app.controller import create_api  # pragma: no cover
from app.utils.arg_parser import parse_api_args  # pragma: no cover
from app.utils.common import load_config  # pragma: no cover

api = create_api(load_config(parse_api_args()))  # pragma: no cover
