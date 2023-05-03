"""This module contains objects for authenticating with the TFL API.

Using the `Auth` class, you can authenticate with the TFL API using your API key. When a request is sent, the API key
will be added to the request URL.

You can register for an API key via the TFL [API website](https://api-portal.tfl.gov.uk/signup). An API key is not
required to use the TFL API. However, without registering for an API key, you will be limited to 50 requests per hour.
If an invalid API key is provided an error by the TFL API will be returned.
"""

from typing import Any, Generator

import httpx

__all__ = ["Auth"]


class Auth(httpx.Auth):
    """The authentication class for Transport for London API.

    Using the `Auth` class, you can authenticate with the TFL API using your API key. When a request is sent, the API
    key will be added to the request URL.

    Example:
        ```python
        from tfl import clients

        async with clients.LiftDisruptionsV2Client(auth=clients.Auth("<your-tfl-api-key>")) as client:
            response = await client.get_lift_disruptions()

        print(response.json())
        ```

    Args:
        key: The TFL API key.
    """

    def __init__(self, key: str) -> None:
        self.key = key

    def auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, Any, None]:
        """Add the API key to the request.

        The key will be added to the request URL as a query parameter.

        Args:
            request: The request to be sent.

        Returns:
            The request with the API key added to the URL.
        """
        request.url = request.url.copy_add_param(key="app_key", value=self.key)
        yield request
