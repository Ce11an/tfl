"""Test the TFLClient class."""

from tfl import clients


class TestTFLClient:
    """Test the TFLClient class."""

    def test_init(self):
        """Test the __init__ method."""
        client = clients.TFLClient()
        assert client.base_url == "https://api.tfl.gov.uk"
        assert client.auth is None
