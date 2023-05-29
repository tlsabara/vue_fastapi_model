import pytest
from api.api_core.bases import on_response
from datetime import datetime


@pytest.fixture()
def fixture_baseapiresponse_instance():
    return on_response.BaseApiResponse(
        time_at=datetime.now(), app_version="0.0.1", api_version="v1"
    )
