![TFL-Image.jpg](https://github.com/Ce11an/tfl/raw/main/assets/TFL-Image.jpg)

[![Python](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)](https://pypi.org/project/py-tfl/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/Ce11an/tfl/blob/main/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/Ce11an/tfl/releases)
![Code Stability](https://github.com/Ce11an/tfl/actions/workflows/stability.yml/badge.svg)
![Unit Tests](https://github.com/Ce11an/tfl/actions/workflows/unit-tests.yml/badge.svg)
[![codecov](https://codecov.io/gh/Ce11an/tfl/branch/main/graph/badge.svg?token=ZR23YMRZVV)](https://codecov.io/gh/Ce11an/tfl)
[![CodeFactor](https://www.codefactor.io/repository/github/ce11an/tfl/badge)](https://www.codefactor.io/repository/github/ce11an/tfl)

A Python package for the [Transport for London (TFL) API](https://api-portal.tfl.gov.uk).

The TFL API is a RESTful API that provides data related to all modes of transport in London, including cycle hire,
buses, roads, and the underground. Anonymous access to the TFL API is limited to 50 requests a minute. If you want to
call the API more than that, you'll need to subscribe to a "Product" which lets you bypass this limit with a
subscription-key that you append to your requests.

Currently, we support the following APIs:

- [Accident Stats API](https://api-portal.tfl.gov.uk/api-details#api=AccidentStats&operation=AccidentStats_Get)
- [Air Quality API](https://api-portal.tfl.gov.uk/api-details#api=AirQuality&operation=AirQuality_Get)
- [Crowding API](https://api-portal.tfl.gov.uk/api-details#api=crowding&operation=dayofweek)
- [Lift Disruptions API](https://api-portal.tfl.gov.uk/api-details#api=Disruptions-Lifts-v2&operation=get)

The plan is to add support for all the TFL APIs. Contributions are welcome!

## Installation

```bash
pip install py-tfl
```

or install with [Poetry](https://python-poetry.org/):

```bash
poetry add py-tfl
```

## ⚡️Quickstart

### ⌨️ CLI
The TFL CLI provides a command line interface to the TFL API. It is built on top of
[Typer](https://typer.tiangolo.com/), which provides easy way to build command line interfaces.

```bash
tfl --help
```

### 🦋 Client
The TFL client provides a Python interface to the TFL API. It provides a Pythonic interface to the API, and handles
authentication and rate limiting for you. The client is built on top of [HTTPX](https://www.python-httpx.org/), which
provides a fast, async HTTP client.

```python
from tfl import clients


async with clients.LiftDisruptionsV2Client() as client:
    response = await client.get_lift_disruptions()

print(response.json())
```

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/Ce11an/tfl/releases)
page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft
release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can
categorize pull requests in release notes using labels.

## 🛡 License

[![License](https://img.shields.io/github/license/Ce11an/tfl)](https://github.com/Ce11an/tfl/blob/main/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/Ce11an/tfl/blob/main/LICENSE)
for more details.

## 🚀 Credits

A special thanks to HTTPX, Typer, and the TFL API team for making this project possible.

This project was built using [IntelliJ IDEA](https://www.jetbrains.com/community/opensource/?utm_campaign=opensource&utm_content=approved&utm_medium=email&utm_source=newsletter&utm_term=jblogo#support).

![JetBrains Black Box Logo logo](https://resources.jetbrains.com/storage/products/company/brand/logos/jb_square.svg)
