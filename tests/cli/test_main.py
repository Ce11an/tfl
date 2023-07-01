"""Test the tfl CLI."""

from typer.testing import CliRunner

from tests.static_vars import (
    ACCIDENT_STATS_AFTER_2020,
    ACCIDENT_STATS_BEFORE_2020,
    AIR_QUALITY,
    CROWDING_NAPTAN,
    LIFT_DISRUPTIONS,
)
from tfl.cli.main import app

runner = CliRunner()

LIFT_DISRUPTIONS_SUCCESS = """                                Lift Disruptions
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃           ┃                                                                  ┃
┃ Station   ┃ Message                                                          ┃
┃           ┃                                                                  ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│           │                                                                  │
│ Shenfield │ Step-free access is not available to the Greater Anglia          │
│           │ platforms 3 and 4 and the Elizabeth line platforms 5 and 6 due   │
│           │ to faulty lifts. Call us on 0343 222 1234 if youneed help        │
│           │ planning your journey.                                           │
│           │                                                                  │
│           │                                                                  │
│ Taplow    │ Step free access is not available between the entrance on Bath   │
│           │ Road and the footbridge. For step free access, use the entrance  │
│           │ on Approach Road. Call 0343 222 1234 if you need help planning   │
│           │ your journey.                                                    │
│           │                                                                  │
└───────────┴──────────────────────────────────────────────────────────────────┘
                         Current TFL lift disruptions.
"""


class TestApp:
    """Test the tfl CLI."""

    def test_version(self) -> None:
        """Test the version command."""
        result = runner.invoke(app, ["--version"])
        assert result.exit_code == 0
        assert "tfl version:" in result.stdout

    def test_help(self) -> None:
        """Test the help command."""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "tfl: A Python package for the Transport for London (TFL) API." in result.stdout

    def test_lift_disruptions(self, httpx_mock) -> None:
        """Test the lift-disruptions command."""
        httpx_mock.add_response(
            url="https://api.tfl.gov.uk/Disruptions/Lifts/v2",
            json=LIFT_DISRUPTIONS,
            method="GET",
        )
        result = runner.invoke(app, ["lift-disruptions"])
        assert result.exit_code == 0
        assert result.stdout == LIFT_DISRUPTIONS_SUCCESS

    def test_lift_disruptions_with_key_env(self, httpx_mock, monkeypatch) -> None:
        """Test the lift-disruptions command with the TFL_API_KEY environment variable."""
        monkeypatch.setenv("TFL_API_KEY", "XXX")
        httpx_mock.add_response(
            url="https://api.tfl.gov.uk/Disruptions/Lifts/v2?app_key=XXX",
            json=LIFT_DISRUPTIONS,
            method="GET",
        )
        result = runner.invoke(app, ["lift-disruptions"])
        assert result.stdout == LIFT_DISRUPTIONS_SUCCESS

    def test_accident_stats_before_2020(self, httpx_mock) -> None:
        """Test the accident-stats command before 2020."""
        httpx_mock.add_response(
            url="https://api.tfl.gov.uk/AccidentStats/2019",
            json=ACCIDENT_STATS_BEFORE_2020,
            method="GET",
        )
        result = runner.invoke(app, ["accident-stats", "2019"])
        assert "[\n" in result.stdout

    def test_accident_stats_after_2020(self, httpx_mock) -> None:
        """Test the accident-stats command after 2020."""
        httpx_mock.add_response(
            url="https://api.tfl.gov.uk/AccidentStats/2020",
            json=ACCIDENT_STATS_AFTER_2020,
            method="GET",
        )
        result = runner.invoke(app, ["accident-stats", "2020"])
        assert "{\n" in result.stdout

    def test_air_quality(self, httpx_mock) -> None:
        """Test the air-quality command."""
        httpx_mock.add_response(
            url="https://api.tfl.gov.uk/AirQuality",
            json=AIR_QUALITY,
            method="GET",
        )
        result = runner.invoke(app, ["air-quality"])
        assert result.exit_code == 0
        assert "{\n" in result.stdout

    def test_get_crowding_day_none(self, httpx_mock) -> None:
        """Test the `get_crowding` method with day as `None`."""
        httpx_mock.add_response(
            url="https://api.tfl.gov.uk/crowding/940GZZLUBND",
            json=CROWDING_NAPTAN,
            method="GET",
        )
        result = runner.invoke(app, ["crowding", "940GZZLUBND"])
        assert "{\n" in result.stdout

    def test_get_crowding_with_day(self, httpx_mock) -> None:
        """Test the `get_crowding` with day as `enums.DayOfWeekEnum`."""
        httpx_mock.add_response(
            url="https://api.tfl.gov.uk/crowding/940GZZLUBND/Fri",
            json=CROWDING_NAPTAN,
            method="GET",
        )
        result = runner.invoke(app, ["crowding", "940GZZLUBND", "Fri"])
        assert "{\n" in result.stdout

    def test_get_crowding_with_invalid_day(self) -> None:
        """Test the `get_crowding` with an invalid day."""
        result = runner.invoke(app, ["crowding", "940GZZLUBND", "Friday"])
        assert isinstance(result.exception, ValueError)
