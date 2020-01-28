from unittest import mock

import pytest
import responses

from pyptax import settings
from pyptax.client import Ptax
from pyptax.exceptions import ClientError


@mock.patch("pyptax.client.requests.get")
@mock.patch("pyptax.resources.CloseResource")
def test_ptax_client(mock_close_resource, mock_request):
    Ptax(mock_close_resource).response()
    assert mock_request.call_count == 1
    assert mock_close_resource.parse.call_count == 1


@responses.activate
@mock.patch("pyptax.resources.CloseResource")
def test_ptax_client_error(mock_close_resource):
    path = "resource_path"
    mock_close_resource.path = path
    mock_close_resource.params = None
    responses.add(responses.GET, f"{settings.SERVICE_URL}{path}", status=500)

    with pytest.raises(ClientError) as exc_info:
        Ptax(mock_close_resource).response()

    assert "Could not retrieve information from Ptax Service" in str(exc_info.value)
