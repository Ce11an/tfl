"""Test the crowding handler class."""

import httpx
import pytest

from tests.static_vars import CROWDING_NAPTAN
from tfl import enums

# noinspection PyProtectedMember
from tfl.clients.handlers._crowding_handler import CrowdingHandler


class TestCrowdingClient:
    """Test the crowding client class."""

    naptan_code = "940GZZLUBND"
    day = "Fri"

    @pytest.mark.asyncio
    async def test_get_crowding_day_none(self, httpx_mock) -> None:
        """Test the `get_crowding` method with day as `None`."""
        httpx_mock.add_response(
            url=f"https://api.tfl.gov.uk/crowding/{self.naptan_code}",
            json=CROWDING_NAPTAN,
            method="GET",
        )
        async with httpx.AsyncClient(base_url="https://api.tfl.gov.uk") as client:
            response = await CrowdingHandler(client).get_crowding(naptan_code=self.naptan_code)
        assert response.status_code == 200
        assert response.json() == CROWDING_NAPTAN

    @pytest.mark.asyncio
    async def test_get_crowding_with_day(self, httpx_mock) -> None:
        """Test the `get_crowding` with day as `enums.DayOfWeekEnum`."""
        httpx_mock.add_response(
            url=f"https://api.tfl.gov.uk/crowding/{self.naptan_code}/{self.day}",
            json=CROWDING_NAPTAN,
            method="GET",
        )
        async with httpx.AsyncClient(base_url="https://api.tfl.gov.uk") as client:
            response = await CrowdingHandler(client).get_crowding(
                naptan_code=self.naptan_code, day=enums.DayOfWeekEnum.FRIDAY
            )
        assert response.status_code == 200
        assert response.json() == CROWDING_NAPTAN
