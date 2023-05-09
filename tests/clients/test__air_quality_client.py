"""Test the air quality client class."""

import pytest

from tests.static_vars import AIR_QUALITY
from tfl import clients


class TestAirQualityClient:
    """Test the lift disruptions v2 client class."""

    @pytest.mark.asyncio
    async def test_lift_disruptions(self, httpx_mock) -> None:
        """Test the `get_air_quality` method."""
        httpx_mock.add_response(
            url="https://api.tfl.gov.uk/AirQuality",
            json=AIR_QUALITY,
            method="GET",
        )
        async with clients.AirQualityClient() as client:
            response = await client.get_air_quality()
        assert response.status_code == 200
        assert response.json() == AIR_QUALITY
