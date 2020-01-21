import responses

from pyptax import ptax
from pyptax import settings
from pyptax.models import CloseReport


@responses.activate
def test_close():
    date = "01-16-2020"

    responses.add(
        responses.GET,
        f"{settings.SERVICE_URL}{settings.CLOSE_RESOURCE}?@dataCotacao={date!r}&$format=json",
        json={
            "value": [
                {
                    "dataHoraCotacao": "2020-01-16 13:04:37.351",
                    "cotacaoCompra": 4.172,
                    "cotacaoVenda": 4.1726,
                }
            ]
        },
    )

    close = ptax.close(date)

    assert len(responses.calls) == 1
    assert isinstance(close, CloseReport)
