"""
FastAPI settings for the project.
"""

import os
from pathlib import Path

# import sentry_sdk
from decouple import Csv, config
from web3 import Web3

from app.enums import Environment

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#######################
# ConfigMap variables #
#######################
ENV = config("ENV")
LOG_LEVEL = config("LOG_LEVEL")
# ALLOWED_HOSTS = set(config('ALLOWED_HOSTS', cast=Csv()))
REQUESTS_TIMEOUT = (3.05, 27)
DEBUG = False
PROJECT_NAME = "Fast API play project"
API_V1_STR: str = "/api/v1"
BACKEND_CORS_ORIGINS = config("BACKEND_CORS_ORIGINS", cast=Csv())

##############
# Blockchain #
##############
# RPC url
RPC_URL = None
INFURA_NETWORK = config("INFURA_NETWORK", None)
if INFURA_NETWORK:  # pragma: no cover
    INFURA_PROJECT_ID = config("INFURA_PROJECT_ID")
    INFURA_PROJECT_SECRET = config("INFURA_PROJECT_SECRET")
    assert INFURA_NETWORK in ["rinkeby", "ropsten", "mainnet"]
    RPC_URL = f"https://:{INFURA_PROJECT_SECRET}@{INFURA_NETWORK}.infura.io/v3/{INFURA_PROJECT_ID}"
else:
    RPC_URL = config("BLOCKCHAIN_RPC_URL")
assert RPC_URL
W3 = Web3(
    Web3.HTTPProvider(
        RPC_URL,
    )
)
ACR_TOKEN_DECIMALS = 18
SECURE_CONFIRMATION_NUMBER = 12

# Contracts
ACR_TOKEN_PROXY_CONTRACT_ADDRESS = config("ACR_TOKEN_PROXY_CONTRACT_ADDRESS")
ABI_PATH = os.path.join(BASE_DIR, "abi")
with open(os.path.join(ABI_PATH, "ACRToken.abi"), "r", encoding="UTF-8") as contract_abi_file:
    ACR_TOKEN_CONTRACT_ABI = contract_abi_file.read()
ACR_TOKEN_PROXY_CONTRACT = W3.eth.contract(address=ACR_TOKEN_PROXY_CONTRACT_ADDRESS, abi=ACR_TOKEN_CONTRACT_ABI)

ACR_NFT_CONTRACT_ADDRESS = config("ACR_NFT_CONTRACT_ADDRESS")
with open(os.path.join(ABI_PATH, "ACRNFT.abi"), "r", encoding="UTF-8") as contract_abi_file:
    ACR_NFT_CONTRACT_ABI = contract_abi_file.read()
ACR_NFT_CONTRACT = W3.eth.contract(address=ACR_NFT_CONTRACT_ADDRESS, abi=ACR_NFT_CONTRACT_ABI)

if ENV == Environment.LOCAL.value:  # pragma: no cover

    DEBUG = True

    BACKEND_CORS_ORIGINS.extend(
        [
            "http://127.0.0.1:8000",
            "http://localhost:8000",
            "http://127.0.0.1:8080",
            "http://localhost:8080",
            "https://127.0.0.1:3000",
            "http://127.0.0.1:3000",
            "https://localhost:3000",
            "http://localhost:3000",
        ]
    )
