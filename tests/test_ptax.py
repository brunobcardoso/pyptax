import responses

from pyptax import ptax


@responses.activate
def test_close():
    date = "01-16-2020"

    responses.add(
        responses.GET,
        f"{ptax.SERVICE_URL}{ptax.RESOURCE}?@dataCotacao={date!r}&$format=json",
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

    expected = {
        "datetime": "2020-01-16 13:04:37.351",
        "bid": "4.1720",
        "ask": "4.1726",
    }

    assert len(responses.calls) == 1
    assert close == expected
