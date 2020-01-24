import pytest

from pyptax.models import CloseReport


@pytest.fixture
def close_report():
    return CloseReport("2019-01-25 12:21", "4.3565", "4.3574")


@pytest.fixture
def close_raw_data():
    return {
        "value": [
            {
                "dataHoraCotacao": "2020-01-16 13:04:37.351",
                "cotacaoCompra": 4.172,
                "cotacaoVenda": 4.1726,
            }
        ]
    }
