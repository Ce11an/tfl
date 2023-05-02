"""Test the Client class."""

import pytest

from tests.static_vars import LIFT_DISRUPTIONS
from tfl import Client


class TestClient:
    """Test the Client class."""

    @pytest.mark.asyncio
    async def test_lift_disruptions(self, httpx_mock) -> None:
        """Test the lift_disruptions method."""
        httpx_mock.add_response(
            url="https://api.tfl.gov.uk/Disruptions/Lifts/v2/",
            json=LIFT_DISRUPTIONS,
            method="GET",
        )
        async with Client() as client:
            response = await client.get_lift_disruptions()
        assert response.status_code == 200
        assert response.json() == LIFT_DISRUPTIONS
