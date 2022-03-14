"""General enums"""
from enum import Enum, unique


@unique
class Environment(Enum):
    """Development/Deployment environments"""

    LOCAL = "LOCAL"
    TEST = "TEST"
    DEV = "DEV"
    STG = "STG"
    PRD = "PRD"
