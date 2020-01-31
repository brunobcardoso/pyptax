import pytest

from pyptax.models import CloseReport
from pyptax.models import HistoricalReport


@pytest.fixture
def close_report():
    return CloseReport("2019-01-25 12:21", 4.3565, 4.3574)


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


@pytest.fixture
def historical_report():
    return HistoricalReport(
        start_date="2020-01-01",
        end_date="2020-01-03",
        reports=[
            CloseReport("2020-01-02 13:11:10.762", 4.0207, 4.0213),
            CloseReport("2020-01-03 13:06:22.606", 4.0516, 4.0522),
        ],
    )


@pytest.fixture
def historical_raw_data():
    return {
        "value": [
            {
                "dataHoraCotacao": "2020-01-02 13:11:10.762",
                "cotacaoCompra": 4.0207,
                "cotacaoVenda": 4.0213,
            },
            {
                "dataHoraCotacao": "2020-01-03 13:06:22.606",
                "cotacaoCompra": 4.0516,
                "cotacaoVenda": 4.0522,
            },
        ]
    }
