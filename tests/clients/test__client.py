"""Test the TFLClient class."""

import pytest

from tests.static_vars import LIFT_DISRUPTIONS
from tfl import clients
from tfl.clients.handlers import TFLHandlers


class TestTFLClient:
    """Test the TFLClient class."""

    def test_init(self):
        """Test the __init__ method."""
        client = clients.TFLClient()
        assert client.base_url == "https://api.tfl.gov.uk"
        assert client.auth is None
        assert isinstance(client.handlers, TFLHandlers)

    @pytest.mark.asyncio
    async def test_handler(self, httpx_mock) -> None:
        """Test handler can be accessed and used."""
        httpx_mock.add_response(
            url="https://api.tfl.gov.uk/Disruptions/Lifts/v2",
            json=LIFT_DISRUPTIONS,
            method="GET",
        )
        async with clients.TFLClient() as client:
            response = await client.handlers.lift_disruptions_v2_handler.get_lift_disruptions()
        assert response.status_code == 200
        assert response.json() == LIFT_DISRUPTIONS
