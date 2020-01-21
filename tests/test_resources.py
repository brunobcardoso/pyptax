from pyptax.models import CloseReport
from pyptax.resources import CloseResource


def test_close_resource():
    date = "17-01-2020"
    resource = CloseResource(date)
    assert resource.date == date
    assert resource.params == f"@dataCotacao={date!r}&$format=json"


def test_close_resource_parse():
    raw_data = {
        "value": [
            {
                "dataHoraCotacao": "2020-01-16 13:04:37.351",
                "cotacaoCompra": 4.172,
                "cotacaoVenda": 4.1726,
            },
        ]
    }

    assert isinstance(CloseResource("16-01-2020").parse(raw_data), CloseReport)
