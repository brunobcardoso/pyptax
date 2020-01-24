def test_close_report(close_report):
    assert close_report.datetime == "2019-01-25 12:21"
    assert close_report.bid == "4.3565"
    assert close_report.ask == "4.3574"


def test_close_report_str(close_report):
    expected = "2019-01-25 12:21 - bid: 4.3565 - ask: 4.3574"
    assert str(close_report) == expected


def test_close_report_repr(close_report):
    expected = "CloseReport(datetime=2019-01-25 12:21, bid=4.3565, ask=4.3574)"
    assert repr(close_report) == expected


def test_close_report_as_dict(close_report):
    expected = {
        "datetime": "2019-01-25 12:21",
        "bid": "4.3565",
        "ask": "4.3574",
    }
    assert close_report.as_dict == expected
