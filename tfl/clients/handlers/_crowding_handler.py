"""Handler to interact with the crowding API."""

from typing import Optional

import httpx

from tfl import base, enums

__all__ = ["CrowdingHandler"]


class CrowdingHandler(base.TFLHandler):
    """Handler to interact with the Crowding API.

    [API reference](https://api-portal.tfl.gov.uk/api-details#api=crowding&operation=dayofweek)

    Example:
        ```python
        from tfl import clients, enums

        async with clients.TFLClient(auth=clients.Auth(key="<your-tfl-api-key>")) as client:
            response = await CrowdingHandler(client).get_crowding(
                naptan_code="940GZZLUBND", day=enums.DayOfWeekEnum.MONDAY
            )

        print(response.json())
        ```
    """

    async def get_crowding(self, naptan_code: str, day: Optional[enums.DayOfWeekEnum] = None) -> httpx.Response:
        """Get information about crowding levels within TFL stations.

        Args:
            naptan_code: The NAPTAN code of the station to get crowding information for.
            day: The day to get crowding information for.

        Returns:
            The response from the API.
        """
        _url = f"crowding/{naptan_code}"
        if day:
            _url += f"/{day.value}"
        return await self.client.get(url=_url)
