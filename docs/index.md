# tfl

<div align="center">

![TFL-Image.jpg](..%2Fassets%2FTFL-Image.jpg)

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/Ce11an/tfl/blob/main/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/Ce11an/tfl/releases)
![Code Stability](https://github.com/Ce11an/tfl/actions/workflows/stability.yml/badge.svg)
![Unit Tests](https://github.com/Ce11an/tfl/actions/workflows/unit-tests.yml/badge.svg)

A Python package for the Transport for London (TFL) API.

</div>

*Disclaimer*: This project is not affiliated with Transport for London.

This project is a Python client for the [Transport for London API](https://api-portal.tfl.gov.uk). It is a work in
progress and is not yet ready for use.

The TFL API is a RESTful API that provides data related to all modes of transport in London, including cycle hire,
buses, roads, and the underground. Anonymous access to the TFL API is limited to 50 requests a minute. If you want to
call the API more than that, you'll need to subscribe to a "Product" which lets you bypass this limit with a
subscription-key that you append to your requests.


## Installation

```bash
poetry install
```

## Quickstart

### CLI
The TFL CLI provides a command line interface to the TFL API. It is built on top of 
[Typer](https://typer.tiangolo.com/), which provides easy way to build command line interfaces.

```bash
poetry run tfl --help
```

### Client
The TFL client provides a Python interface to the TFL API. It provides a Pythonic interface to the API, and handles
authentication and rate limiting for you. The client is built on top of [HTTPX](https://www.python-httpx.org/), which 
provides a fast, async HTTP client.

```python
from tfl import clients

async with clients.LiftDisruptionsV2Client() as client:
    response = await client.get_lift_disruptions()
    
print(response.json())
```
