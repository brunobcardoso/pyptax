from pyptax.models import CloseReport


def test_close_report():
    close_report = CloseReport("2019-01-25 12:21", "4.3565", "4.3574")
    assert close_report.datetime == "2019-01-25 12:21"
    assert close_report.bid == "4.3565"
    assert close_report.ask == "4.3574"


def test_close_report_str():
    expected = "2019-01-25 12:21 - bid: 4.3565 - ask: 4.3574"
    assert str(CloseReport("2019-01-25 12:21", "4.3565", "4.3574")) == expected


def test_close_report_repr():
    expected = "CloseReport(datetime=2019-01-25 12:21, bid=4.3565, ask=4.3574)"
    assert repr(CloseReport("2019-01-25 12:21", "4.3565", "4.3574")) == expected


def test_close_report_as_dict():
    expected = {
        "datetime": "2019-01-25 12:21",
        "bid": "4.3565",
        "ask": "4.3574",
    }
    assert CloseReport("2019-01-25 12:21", "4.3565", "4.3574").as_dict == expected
