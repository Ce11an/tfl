"""Test the CLI module."""

import asyncio

import pytest

from tfl.cli import AsyncTyper


@pytest.mark.asyncio
async def test_async_command() -> None:
    """Test the async_command decorator."""
    app = AsyncTyper()

    @app.async_command()
    async def hello() -> None:
        """Say hello."""
        await asyncio.sleep(1)
        print("Hello!")

    await hello()
    assert True
