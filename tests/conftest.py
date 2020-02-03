import pytest

from pyptax.models import Bulletin, HistoricalBulletin


@pytest.fixture
def bulletin():
    return Bulletin("2019-01-25 12:21", 4.3565, 4.3574, "close")


@pytest.fixture
def close_raw_data():
    return {
        "value": [
            {
                "dataHoraCotacao": "2020-01-16 13:04:37.351",
                "cotacaoCompra": 4.172,
                "cotacaoVenda": 4.1726,
                "bulletin_type": "close",
            }
        ]
    }


@pytest.fixture
def historical_bulletin():
    return HistoricalBulletin(
        start_date="2020-01-01",
        end_date="2020-01-03",
        bulletins=[
            Bulletin("2020-01-02 13:11:10.762", 4.0207, 4.0213, "close"),
            Bulletin("2020-01-03 13:06:22.606", 4.0516, 4.0522, "close"),
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


@pytest.fixture
def intermediary_raw_data():
    return {
        "value": [
            {
                "cotacaoCompra": 4.0101,
                "cotacaoVenda": 4.0107,
                "dataHoraCotacao": "2020-01-02 10:08:18.114",
                "tipoBoletim": "Abertura",
            },
            {
                "cotacaoCompra": 4.0118,
                "cotacaoVenda": 4.0124,
                "dataHoraCotacao": "2020-01-02 11:03:40.704",
                "tipoBoletim": "Intermediário",
            },
            {
                "cotacaoCompra": 4.0302,
                "cotacaoVenda": 4.0308,
                "dataHoraCotacao": "2020-01-02 12:10:55.168",
                "tipoBoletim": "Intermediário",
            },
            {
                "cotacaoCompra": 4.0305,
                "cotacaoVenda": 4.0311,
                "dataHoraCotacao": "2020-01-02 13:11:10.756",
                "tipoBoletim": "Intermediário",
            },
            {
                "cotacaoCompra": 4.0207,
                "cotacaoVenda": 4.0213,
                "dataHoraCotacao": "2020-01-02 13:11:10.762",
                "tipoBoletim": "Fechamento PTAX",
            },
        ]
    }
