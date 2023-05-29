from datetime import datetime

import pytest
import os
from dotenv import load_dotenv
from api.api_core.bases import on_request, on_response
from fastapi.testclient import TestClient
from api.entry import __version__, app
from .fixtures import fixture_baseapiresponse_instance

load_dotenv()
os.environ["APP_VERSION"] = __version__


class TestPingPongRequestBoddy:
    def test_attrs_on_pinigpongrequestboddy_class(self) -> None:
        """Assert if request body object has the expected attrs."""
        instance_ = on_request.PingPongRequestBody(song="A", name="B")
        assert hasattr(instance_, "song")
        assert hasattr(instance_, "name")


class TestBaseApiResponse:
    def test_attrs_on_baseapiresponse_class(
        self, fixture_baseapiresponse_instance
    ) -> None:
        """Tests if the base format of project has all defined attrs"""
        instance_ = fixture_baseapiresponse_instance
        assert hasattr(instance_, "app_version")
        assert hasattr(instance_, "api_version")
        assert hasattr(instance_, "time_at")
        assert hasattr(instance_, "method")

    @pytest.mark.parametrize("target_method", ["GET", "PUT", "POST", "DELETE"])
    def test_function_set_http_method(
        self, fixture_baseapiresponse_instance: pytest.fixture, target_method: str
    ) -> None:
        """Tests if function set_http_method apply the specified methods"""
        instance_ = fixture_baseapiresponse_instance
        instance_.set_http_method(target_method)

        assert instance_.method == target_method

    def test_if_function_set_http_method_raises_error_with_invalid_method(
        self, fixture_baseapiresponse_instance: pytest.fixture
    ) -> None:
        instance_ = fixture_baseapiresponse_instance
        with pytest.raises(ValueError) as e:
            instance_.set_http_method("Catapimbas")
        assert "Method Invalid." == str(e.value)
