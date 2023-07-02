"""Test the air quality handler class."""

import httpx
import pytest

from tests.static_vars import AIR_QUALITY

# noinspection PyProtectedMember
from tfl.clients.handlers._air_quality_handler import AirQualityHandler


class TestAirQualityClient:
    """Test the air quality handler class."""

    @pytest.mark.asyncio
    async def test_air_quality(self, httpx_mock) -> None:
        """Test the `get_air_quality` method."""
        httpx_mock.add_response(
            url="https://api.tfl.gov.uk/AirQuality",
            json=AIR_QUALITY,
            method="GET",
        )
        async with httpx.AsyncClient(base_url="https://api.tfl.gov.uk") as client:
            response = await AirQualityHandler(client).get_air_quality()
        assert response.status_code == 200
        assert response.json() == AIR_QUALITY
