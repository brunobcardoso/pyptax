import pytest

from pyptax.exceptions import UnavailableDataError
from pyptax.models import CloseReport
from pyptax.resources import CloseResource


def test_close_resource_params():
    date = "2020-02-01"
    resource = CloseResource(date)
    assert resource.params == f"@dataCotacao={resource.parsed_date!r}&$format=json"


def test_close_resource_parse(close_raw_data):
    assert isinstance(CloseResource("2020-01-16").parse(close_raw_data), CloseReport)


def test_close_resource_parse_error():
    with pytest.raises(UnavailableDataError) as exc_info:
        CloseResource("2020-01-16").parse({"value": []})

    assert "Unavailable rates for the requested date" in str(exc_info.value)
