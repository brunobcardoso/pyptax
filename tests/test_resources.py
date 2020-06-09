import pytest

from pyptax.exceptions import UnavailableDataError
from pyptax.models import Bulletin, HistoricalBulletin, IntermediaryBulletin
from pyptax.resources import CloseResource, HistoricalResource, IntermediaryResource


def test_close_resource_params():
    resource = CloseResource("2020-02-01")
    assert resource.params == "@dataCotacao='02-01-2020'&$format=json"


def test_close_resource_parse(close_raw_data):
    assert isinstance(CloseResource("2020-01-16").parse(close_raw_data), Bulletin)


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
    assert isinstance(parsed, HistoricalBulletin)
    assert parsed.bulletins == [
        Bulletin("2020-01-02 13:11:10.762", 4.0207, 4.0213, "close",),
        Bulletin("2020-01-03 13:06:22.606", 4.0516, 4.0522, "close",),
    ]


def test_historical_resource_parse_error():
    with pytest.raises(UnavailableDataError) as exc_info:
        HistoricalResource("2020-01-01", "2020-01-03").parse({"value": []})

    assert "Unavailable rates for the requested range" in str(exc_info.value)


def test_intermediary_resource_params():
    resource = IntermediaryResource("2020-01-02")
    expected = "@moeda='USD'&@dataCotacao='01-02-2020'&$format=json"
    assert resource.params == expected


def test_intermediary_resource_parse_error():
    with pytest.raises(UnavailableDataError) as exc_info:
        IntermediaryResource("2020-01-01").parse({"value": []})

    assert "Unavailable rates for the requested date" in str(exc_info.value)


def test_intermediary_resource_parse(intermediary_raw_data):
    resource = IntermediaryResource("2020-01-02")
    parsed = resource.parse(intermediary_raw_data)
    assert isinstance(parsed, IntermediaryBulletin)
    assert parsed.bulletins == [
        Bulletin("2020-01-02 10:08:18.114", 4.0101, 4.0107, "open"),
        Bulletin("2020-01-02 11:03:40.704", 4.0118, 4.0124, "intermediary"),
        Bulletin("2020-01-02 12:10:55.168", 4.0302, 4.0308, "intermediary"),
        Bulletin("2020-01-02 13:11:10.756", 4.0305, 4.0311, "intermediary"),
        Bulletin("2020-01-02 13:11:10.762", 4.0207, 4.0213, "close"),
    ]
