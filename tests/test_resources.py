import pytest

from pyptax.exceptions import UnavailableDataError
from pyptax.models import CloseReport
from pyptax.models import HistoricalReport
from pyptax.resources import CloseResource
from pyptax.resources import HistoricalResource


def test_close_resource_params():
    resource = CloseResource("2020-02-01")
    assert resource.params == f"@dataCotacao='02-01-2020'&$format=json"


def test_close_resource_parse(close_raw_data):
    assert isinstance(CloseResource("2020-01-16").parse(close_raw_data), CloseReport)


def test_close_resource_parse_error():
    with pytest.raises(UnavailableDataError) as exc_info:
        CloseResource("2020-01-16").parse({"value": []})

    assert "Unavailable rates for the requested date" in str(exc_info.value)


def test_historical_resource_params():
    resource = HistoricalResource("2020-01-01", "2020-01-03")
    expected = "@dataInicial='01-01-2020'&@dataFinalCotacao='01-03-2020'&$format=json"
    assert resource.params == expected


def test_historical_resource_parse(historical_raw_data):
    resource = HistoricalResource("2020-01-01", "2020-01-03")
    parsed = resource.parse(historical_raw_data)
    assert isinstance(parsed, HistoricalReport)
    assert parsed.reports == [
        CloseReport("2020-01-02 13:11:10.762", 4.0207, 4.0213),
        CloseReport("2020-01-03 13:06:22.606", 4.0516, 4.0522),
    ]


def test_historical_resource_parse_error():
    with pytest.raises(UnavailableDataError) as exc_info:
        HistoricalResource("2020-01-01", "2020-01-03").parse({"value": []})

    assert "Unavailable rates for the requested range" in str(exc_info.value)
