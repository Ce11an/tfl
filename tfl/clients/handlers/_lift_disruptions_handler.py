"""A handler to interact with the Lift Disruptions V2 API."""

import httpx

from tfl import base

__all__ = ["LiftDisruptionsV2Handler"]


class LiftDisruptionsV2Handler(base.TFLHandler):
    """A handler to interact with the Lift Disruptions V2 API.

    [API reference](https://api-portal.tfl.gov.uk/api-details#api=Disruptions-Lifts-v2&operation=get)

    Example:
        ```python
        from tfl import clients

        async with clients.TFLClient(auth=clients.Auth(key="<your-tfl-api-key>")) as client:
            response = await LiftDisruptionsV2Handler(client).get_lift_disruptions()

        print(response.json())
        ```
    """

    async def get_lift_disruptions(self) -> httpx.Response:
        """Get all current lift disruptions.

        Returns:
            The response from the API.
        """
        return await self.client.get(url="Disruptions/Lifts/v2")
