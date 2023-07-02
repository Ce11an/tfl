"""Handlers for the TFL API.

The `TFLHandlers` class is used to store all handlers. Using the `TFLHandlers` class, you can access all the TFL API
when using the `TFLClient` class.
"""

import httpx

from tfl.clients.handlers._accident_stats_handler import AccidentStatsHandler
from tfl.clients.handlers._air_quality_handler import AirQualityHandler
from tfl.clients.handlers._crowding_handler import CrowdingHandler
from tfl.clients.handlers._lift_disruptions_handler import LiftDisruptionsV2Handler

__all__ = ["TFLHandlers"]


class TFLHandlers:
    """A class to store all handlers.

    Args:
        client: The TFL client to use when sending requests.
    """

    def __init__(self, client: httpx.AsyncClient) -> None:
        self.lift_disruptions_v2_handler = LiftDisruptionsV2Handler(client)
        self.crowding_handler = CrowdingHandler(client)
        self.air_quality_handler = AirQualityHandler(client)
        self.accident_stats_handler = AccidentStatsHandler(client)
