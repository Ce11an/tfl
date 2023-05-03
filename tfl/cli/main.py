"""Main module for the tfl CLI."""

from typing import Annotated, Optional

import rich
import typer

import tfl
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


# noinspection PyUnusedLocal
@app.callback()
def main(
    version: Annotated[
        bool, typer.Option("--version", callback=version_callback, is_eager=True, help="Show the version and exit.")
    ] = False
) -> None:
    """tfl: A Python package for the Transport for London (TFL) API."""
    return None
