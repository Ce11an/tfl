"""Test the accident stats client class."""

import pytest

from tests.static_vars import ACCIDENT_STATS_AFTER_2020, ACCIDENT_STATS_BEFORE_2020, LIFT_DISRUPTIONS
from tfl import clients


class TestLiftDisruptionsV2Client:
    """Test the accident stats client class."""

    @pytest.mark.asyncio
    async def test_before_2020(self, httpx_mock) -> None:
        """Test the accident_stats method before 2020."""
        httpx_mock.add_response(
            url="https://api.tfl.gov.uk/AccidentStats/2019",
            json=ACCIDENT_STATS_BEFORE_2020,
            method="GET",
        )
        async with clients.AccidentStatsClient() as client:
            response = await client.get_accident_stats(2019)
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
        async with clients.AccidentStatsClient() as client:
            response = await client.get_accident_stats(2020)
        assert response.status_code == 200
        assert response.json() == ACCIDENT_STATS_AFTER_2020
