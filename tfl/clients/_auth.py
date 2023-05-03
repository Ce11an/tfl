"""This module contains the Auth class for the Transport for London API."""

from collections.abc import Generator
from typing import Any

import httpx

__all__ = ["Auth"]


class Auth(httpx.Auth):
    """Auth class for Transport for London API.

    Args:
        key: The TFL API key.
    """

    def __init__(self, key: str) -> None:
        self.key = key

    def auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, Any, None]:
        """Add the API key to the request.

        Args:
            request: The request to be sent.

        Returns:
            The request with the API key added.
        """
        request.url = request.url.copy_add_param(key="app_key", value=self.key)
        yield request
