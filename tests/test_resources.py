from pyptax.models import CloseReport
from pyptax.resources import CloseResource


def test_close_resource_params():
    date = "2020-02-01"
    resource = CloseResource(date)
    assert resource.params == f"@dataCotacao={resource.date!r}&$format=json"


def test_close_resource_parse(close_raw_data):
    assert isinstance(CloseResource("2020-01-16").parse(close_raw_data), CloseReport)
