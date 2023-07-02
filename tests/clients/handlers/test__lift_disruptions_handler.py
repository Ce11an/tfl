"""Test the lift disruptions v2 handler class."""

import httpx
import pytest

from tests.static_vars import LIFT_DISRUPTIONS

# noinspection PyProtectedMember
from tfl.clients.handlers._lift_disruptions_handler import LiftDisruptionsV2Handler


class TestLiftDisruptionsV2Client:
    """Test the lift disruptions v2 client class."""

    @pytest.mark.asyncio
    async def test_handler(self, httpx_mock) -> None:
        """Test handler can be accessed and used."""
        httpx_mock.add_response(
            url="https://api.tfl.gov.uk/Disruptions/Lifts/v2",
            json=LIFT_DISRUPTIONS,
            method="GET",
        )
        async with httpx.AsyncClient(base_url="https://api.tfl.gov.uk") as client:
            response = await LiftDisruptionsV2Handler(client).get_lift_disruptions()
        assert response.status_code == 200
        assert response.json() == LIFT_DISRUPTIONS
