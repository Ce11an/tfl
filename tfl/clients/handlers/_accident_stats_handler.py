"""Handler to interact with the accident stats API."""

import httpx

from tfl import base

__all__ = ["AccidentStatsHandler"]


class AccidentStatsHandler(base.TFLHandler):
    """Handler to interact with the accident stats API.

    [API reference](https://api-portal.tfl.gov.uk/api-details#api=AccidentStats&operation=AccidentStats_Get)

    As it stands, the API does not include data between 2020 and 2023.

    Example:
        ```python
        from tfl import clients


        async with clients.TFLClient(auth=clients.Auth(key="<your-tfl-api-key>")) as client:
            response = await AccidentStatsHandler(client).get_accident_stats()

        print(response.json())
        ```
    """

    async def get_accident_stats(self, year: int) -> httpx.Response:
        """Gets all accident details for accidents occurring in the specified year.

        Returns:
            The response from the API.
        """
        return await self.client.get(url=f"/AccidentStats/{year}")
