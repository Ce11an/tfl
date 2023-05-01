"""Lift Disruptions Models."""
from collections.abc import Iterator

import pydantic

__all__ = ["LiftDisruptionsV2ResponseModel"]


class _LiftDisruptionsV2ResponseModel(pydantic.BaseModel):
    """Lift Disruptions V2 Response Model.

    Model relates to request URL: GET https://api.tfl.gov.uk/Disruptions/Lifts/v2/

    Args:
        station_unique_id: The unique identifier of the station.
        disrupted_lift_unique_ids: The unique identifiers of the disrupted lifts.
        message: A message describing the disruption.
    """

    station_unique_id: str = pydantic.Field(
        ...,
        alias="stationUniqueId",
        title="Station Unique ID",
        description="The unique identifier of the station.",
    )
    disrupted_lift_unique_ids: list[str] = pydantic.Field(
        ...,
        alias="disruptedLiftUniqueIds",
        title="Disrupted Lift Unique IDs",
        description="The unique identifiers of the disrupted lifts.",
    )
    message: str = pydantic.Field(
        ...,
        title="Message",
        description="A message describing the disruption.",
    )

    class Config:
        """Pydantic model configuration."""

        allow_population_by_field_name = True


class LiftDisruptionsV2ResponseModel(pydantic.BaseModel):
    """Lift Disruptions V2 Response.

    Model relates to request URL: GET https://api.tfl.gov.uk/Disruptions/Lifts/v2/

    Args:
        __root__: A list of lift disruptions.
    """

    __root__: list[_LiftDisruptionsV2ResponseModel]

    def __iter__(self) -> Iterator[_LiftDisruptionsV2ResponseModel]:  # type: ignore[override]
        """Iterate over the lift disruptions."""
        return iter(self.__root__)

    def __getitem__(self, item: int) -> _LiftDisruptionsV2ResponseModel:
        """Get a lift disruption by index."""
        return self.__root__[item]

    class Config:
        """Pydantic model configuration."""

        allow_population_by_field_name = True
