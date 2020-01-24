import responses

from pyptax import ptax
from pyptax import settings
from pyptax.models import CloseReport


@responses.activate
def test_close(close_raw_data):
    date = "2020-01-16"

    responses.add(
        responses.GET,
        f"{settings.SERVICE_URL}{settings.CLOSE_RESOURCE}?@dataCotacao='01-16-2020'&$format=json",
        json=close_raw_data,
    )

    close = ptax.close(date)

    assert len(responses.calls) == 1
    assert isinstance(close, CloseReport)
