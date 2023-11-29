# FastAPI framework tests

[![codecov](https://codecov.io/github/adricu/fastapi-play/graph/badge.svg?token=WQHC01ZDKB)](https://codecov.io/github/adricu/fastapi-play)

This is a toy project to play with [FastAPI](https://github.com/tiangolo/fastapi) and some standard smart contracts that can be found in [this other GitHub repository](https://github.com/adricu/avax-play).

To make the project work it can point to these already deployed Smart Contracts:

##  ERC20 with transparent proxy

It has been deployed to Avalanche test network Fuji and can be found [here](https://testnet.snowtrace.io/token/0xA3213f4B06292c5b1D47fBaEBa7051727b8567Bd).

## ERC721 with public mint and whitelisting

It has been deployed to Avalanche test network Fuji and can be found [here](https://testnet.snowtrace.io/token/0x73580eD3d8c9447b1092E508A432a7D50c95Fb7c).

## Run the server

You have to install all the dependencies with [Pipenv](https://github.com/pypa/pipenv) and then run:

`uvicorn app.main:app --reload`

## OpenAPI docs

For each version of the API an OpenAPI UI will be exposed in different endpoints. For example the version 1 of the API can be found at: 

`http://127.0.0.1:8000/api/v1/docs`

The general docs that points to the diferent API available versions is at:

`http://127.0.0.1:8000/docs`
