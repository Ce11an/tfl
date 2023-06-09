"""Main module for the tfl CLI."""

from typing import Any, Dict, Optional, Tuple

import rich
import typer
from rich.console import Console
from rich.table import Table
from typing_extensions import Annotated

import tfl
import tfl.enums
from tfl import cli, clients

app = cli.AsyncTyper()
console = Console()


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

    def _create_table_row(resp_json: Dict[str, Any]) -> Tuple[str, str]:
        """Create a table row from a disruption."""
        split_message = resp_json["message"].split(":")
        return split_message[0], split_message[1].replace(" No Step Free Access - ", "")

    async with clients.TFLClient(auth=tfl.clients.Auth(key=key) if key else None) as client:
        response = await client.handlers.lift_disruptions_v2_handler.get_lift_disruptions()
    table = Table(
        "Station",
        "Message",
        title="Lift Disruptions",
        caption="Current TFL lift disruptions.",
        expand=True,
        padding=(1, 1),
    )
    for disruption in response.json():
        table.add_row(*_create_table_row(disruption))
    console.print(table)
    raise typer.Exit()


@app.async_command()
async def accident_stats(
    year: Annotated[int, typer.Argument(help="The year to get accident stats for.")],
    key: Annotated[Optional[str], typer.Argument(envvar="TFL_API_KEY", help="TFL API key.")] = None,
) -> None:
    """Gets all accident details for accidents occurring in the specified year."""
    async with clients.TFLClient(auth=tfl.clients.Auth(key=key) if key else None) as client:
        response = await client.handlers.accident_stats_handler.get_accident_stats(year=year)
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
    async with clients.TFLClient(auth=tfl.clients.Auth(key=key) if key else None) as client:
        response = await client.handlers.crowding_handler.get_crowding(naptan_code=naptan_code, day=day)
    rich.print(response.json())
    raise typer.Exit()


@app.async_command()
async def air_quality(
    key: Annotated[Optional[str], typer.Argument(envvar="TFL_API_KEY", help="TFL API key.")] = None,
) -> None:
    """Get air quality data feed."""

    def _create_table_row(resp_json: Dict[str, Any]) -> Tuple[str, str]:
        """Create a table row from a air quality response."""
        current_forecast = resp_json["currentForecast"][0]
        return current_forecast["forecastBand"], current_forecast["forecastSummary"]

    async with clients.TFLClient(auth=tfl.clients.Auth(key=key) if key else None) as client:
        response = await client.handlers.air_quality_handler.get_air_quality()

    data = response.json()
    table = Table(
        "Air Pollution Banding",
        "Summary",
        title="Today's Air Quality",
        caption=f"{data['disclaimerText']} \n\nFor more information, please visit: {data['forecastURL']}",
        expand=True,
        padding=(1, 1),
        caption_justify="left",
    )
    table.add_row(*_create_table_row(data))
    console.print(table)
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
