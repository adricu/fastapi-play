"""Argument parser."""
import argparse
from argparse import ArgumentParser
from collections.abc import Sequence
from typing import Optional

from app.utils.common import ENVIRONMENTS, Environment


class ApiArgs(argparse.Namespace):  # pylint: disable=too-few-public-methods
    """API aruments namespace."""

    environment: Environment


def parse_api_args(args: Optional[Sequence[str]] = None) -> Environment:
    """Return environment after parsing app args."""
    parser = ArgumentParser()
    parser.add_argument("environment", type=Environment, choices=ENVIRONMENTS)
    parsed_args = parser.parse_args(args, namespace=ApiArgs)
    return parsed_args.environment
