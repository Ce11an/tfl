"""Main module for the tfl CLI."""

from typing import Optional

import rich
import typer
from typing_extensions import Annotated

import tfl
import tfl.enums
from tfl import cli, clients

app = cli.AsyncTyper()


def version_callback(version: bool) -> None:
    """Print the version of tfl."""
    if version:
        rich.print(f"tfl version: {tfl.__version__}")
        raise typer.Exit()


@app.async_command()
async def lift_disruptions(
    key: Annotated[Optional[str], typer.Argument(envvar="TFL_API_KEY", help="TFL API key.")] = None,
) -> None:
    """Get current lift disruptions."""
    async with clients.LiftDisruptionsV2Client(auth=tfl.clients.Auth(key=key) if key else None) as client:
        response = await client.get_lift_disruptions()
    rich.print(response.json())
    raise typer.Exit()


@app.async_command()
async def accident_stats(
    year: Annotated[int, typer.Argument(help="The year to get accident stats for.")],
    key: Annotated[Optional[str], typer.Argument(envvar="TFL_API_KEY", help="TFL API key.")] = None,
) -> None:
    """Gets all accident details for accidents occurring in the specified year."""
    async with clients.AccidentStatsClient(auth=tfl.clients.Auth(key=key) if key else None) as client:
        response = await client.get_accident_stats(year=year)
    rich.print(response.json())
    raise typer.Exit()


@app.async_command()
async def crowding(
    naptan_code: Annotated[str, typer.Argument(help="The NAPTAN code of the station to get crowding for.")],
    day: Annotated[
        Optional[str],
        typer.Argument(
            help="The day to get crowding information for. The options are 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', "
            "'Sun', 'Live'."
        ),
    ] = None,
    key: Annotated[Optional[str], typer.Argument(envvar="TFL_API_KEY", help="TFL API key.")] = None,
) -> None:
    """Information about crowding levels within TFL stations."""
    day = tfl.enums.DayOfWeekEnum(day) if day else None
    async with clients.CrowdingClient(auth=tfl.clients.Auth(key=key) if key else None) as client:
        response = await client.get_crowding(naptan_code=naptan_code, day=day)
    rich.print(response.json())
    raise typer.Exit()


@app.async_command()
async def air_quality(
    key: Annotated[Optional[str], typer.Argument(envvar="TFL_API_KEY", help="TFL API key.")] = None,
) -> None:
    """Get air quality data feed."""
    async with clients.AirQualityClient(auth=tfl.clients.Auth(key=key) if key else None) as client:
        response = await client.get_air_quality()
    rich.print(response.json())
    raise typer.Exit()


# noinspection PyUnusedLocal
@app.callback()
def main(
    version: Annotated[
        bool, typer.Option("--version", callback=version_callback, is_eager=True, help="Show the version and exit.")
    ] = False
) -> None:
    """tfl: A Python package for the Transport for London (TFL) API."""
    return None
