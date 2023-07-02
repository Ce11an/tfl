"""Test the accident stats handler class."""

import httpx
import pytest

from tests.static_vars import ACCIDENT_STATS_AFTER_2020, ACCIDENT_STATS_BEFORE_2020, LIFT_DISRUPTIONS

# noinspection PyProtectedMember
from tfl.clients.handlers._accident_stats_handler import AccidentStatsHandler


class TestAccidentStatsHandler:
    """Test the accident stats client class."""

    @pytest.mark.asyncio
    async def test_before_2020(self, httpx_mock) -> None:
        """Test the accident_stats method before 2020."""
        httpx_mock.add_response(
            url="https://api.tfl.gov.uk/AccidentStats/2019",
            json=ACCIDENT_STATS_BEFORE_2020,
            method="GET",
        )
        async with httpx.AsyncClient(base_url="https://api.tfl.gov.uk") as client:
            response = await AccidentStatsHandler(client).get_accident_stats(2019)
        assert response.status_code == 200
        assert response.json() == ACCIDENT_STATS_BEFORE_2020

    @pytest.mark.asyncio
    async def test_after_2020(self, httpx_mock) -> None:
        """Test the accident_stats method after 2020."""
        httpx_mock.add_response(
            url="https://api.tfl.gov.uk/AccidentStats/2020",
            json=ACCIDENT_STATS_AFTER_2020,
            method="GET",
        )
        async with httpx.AsyncClient(base_url="https://api.tfl.gov.uk") as client:
            response = await AccidentStatsHandler(client).get_accident_stats(2020)
        assert response.status_code == 200
        assert response.json() == ACCIDENT_STATS_AFTER_2020
