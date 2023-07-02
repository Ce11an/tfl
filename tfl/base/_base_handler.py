"""A base class for all tfl handlers."""

import abc

import httpx

__all__ = ["TFLHandler"]


class TFLHandler(abc.ABC):
    """A base class for all tfl handlers.

    Args:
        client: The client to use when sending requests.

    Raises:
        ValueError: If the client does not have a base URL of https://api.tfl.gov.uk.
    """

    def __init__(self, client: httpx.AsyncClient) -> None:
        if client.base_url != "https://api.tfl.gov.uk":
            raise ValueError("The client must have a base URL of https://api.tfl.gov.uk")
        self.client = client
