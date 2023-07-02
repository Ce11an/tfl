"""Test the base handler class."""

import httpx
import pytest

from tfl.base import TFLHandler


class TestBaseHandler:
    """Test the base handler class."""

    def test_raise_error_base_url(self) -> None:
        """Test an error is raised if the client does not have the correct base URL."""
        with pytest.raises(ValueError):
            TFLHandler(httpx.AsyncClient(base_url="https://api.tfl.com"))
