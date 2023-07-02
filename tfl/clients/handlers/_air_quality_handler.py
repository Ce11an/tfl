"""Handler to interact with the air quality API."""

import httpx

from tfl import base

__all__ = ["AirQualityHandler"]


class AirQualityHandler(base.TFLHandler):
    """Handler to interact with the air quality API.

    [API reference](https://api-portal.tfl.gov.uk/api-details#api=AirQuality&operation=AirQuality_Get)

    Example:
        ```python
        from tfl import clients


        async with clients.TFLClient(auth=clients.Auth(key="<your-tfl-api-key>")) as client:
            response = await AirQualityHandler(client).get_air_quality()

        print(response.json())
        ```
    """

    async def get_air_quality(self) -> httpx.Response:
        """Gets current air quality data feed.

        Returns:
            The response from the API.
        """
        return await self.client.get(url=f"/AirQuality")
