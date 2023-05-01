# tfl

<div align="center">

![TFL-Image.jpg](assets%2FTFL-Image.jpg)

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)

 Transport for London Python client.

</div>

*Disclaimer*: This project is not affiliated with Transport for London.

This project is a Python client for the [Transport for London API](https://api-portal.tfl.gov.uk). It is a work in
progress and is not yet ready for use.

The TFL API is a RESTful API that provides data related to all modes of transport in London, including cycle hire,
buses, roads, and the underground. Anonymous access to the TFL API is limited to 50 requests a minute. If you want to
call the API more than that, you'll need to subscribe to a "Product" which lets you bypass this limit with a
subscription-key that you append to your requests.

# Features
The TFL client provides a Python interface to the TFL API. It provides a Pythonic interface to the API, and handles
authentication and rate limiting for you. It also provides a cache for API responses, so that you don't have to make
the same request twice. The client is built on top of HTTPX, which provides a fast, async HTTP client.

Planned features include:
- [x] Pythonic interface to the TFL API
- [ ] CLI
- [ ] Documentation
- [ ] Tests
- [ ] CI/CD
- [ ] Publish to PyPI


## Installation

    ```bash
    poetry install
    ```
