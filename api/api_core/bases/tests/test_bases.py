import pytest
import os
from dotenv import load_dotenv
from api.api_core.bases import on_request, on_response
from entry import __version__

load_dotenv()
os.environ["APP_VERSION"] = __version__

class TestPingPongRequestBoddy:
    def test_attrs_on_pinigpongrequestboddy_class(self) -> None:
        """Assert if request body object has the expected attrs.
        """
        instance_ = on_request.PingPongRequestBody(song='A', name='B')
        assert hasattr(instance_, 'song')
        assert hasattr(instance_, 'name')


class TestBaseApiResponse:
    def test_attrs_on_baseapiresponse_class(self) -> None:
        # TODO  build this test
        assert False

    def test_function_set_http_method(self) -> None:
        # TODO  build this test
        assert False
