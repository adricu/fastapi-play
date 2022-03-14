"""
FastAPI settings for the project.
"""

import os
from pathlib import Path

# import sentry_sdk
from decouple import config
from web3 import Web3

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#######################
# ConfigMap variables #
#######################
ENV = config("ENV")
LOG_LEVEL = config("LOG_LEVEL")
# ALLOWED_HOSTS = set(config("ALLOWED_HOSTS").split(","))
REQUESTS_TIMEOUT = (3.05, 27)
# DEBUG = False
PROJECT_NAME = "Fast API sample project"
API_V1_STR: str = "/api/v1"

##############
# Blockchain #
##############
# RPC url
RPC_URL = None
INFURA_NETWORK = config("INFURA_NETWORK", None)
if INFURA_NETWORK:
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
