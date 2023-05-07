"""Test the tfl CLI."""
from typer.testing import CliRunner

from tests.static_vars import LIFT_DISRUPTIONS
from tfl.cli.main import app

runner = CliRunner()


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
        assert "[\n" in result.stdout

    def test_lift_disruptions_with_key_env(self, httpx_mock, monkeypatch) -> None:
        """Test the lift-disruptions command with the TFL_API_KEY environment variable."""
        monkeypatch.setenv("TFL_API_KEY", "XXX")
        httpx_mock.add_response(
            url="https://api.tfl.gov.uk/Disruptions/Lifts/v2?app_key=XXX",
            json=LIFT_DISRUPTIONS,
            method="GET",
        )
        result = runner.invoke(app, ["lift-disruptions"])
        assert "[\n" in result.stdout
