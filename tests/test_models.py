def test_close_report(close_report):
    assert close_report.datetime == "2019-01-25 12:21"
    assert close_report.bid == 4.3565
    assert close_report.ask == 4.3574


def test_close_report_repr(close_report):
    expected = "CloseReport(datetime='2019-01-25 12:21', bid=4.3565, ask=4.3574)"
    assert repr(close_report) == expected


def test_close_report_as_dict(close_report):
    expected = {
        "datetime": "2019-01-25 12:21",
        "bid": 4.3565,
        "ask": 4.3574,
    }
    assert close_report.as_dict == expected


def test_close_report_display(close_report):
    expected = (
        "+----------+------------------+\n"
        "| datetime | 2019-01-25 12:21 |\n"
        "| bid      | 4.3565           |\n"
        "| ask      | 4.3574           |\n"
        "+----------+------------------+"
    )
    assert close_report.display() == expected


def test_historical_report_as_dict(historical_report):
    expected = {
        "start_date": "2020-01-01",
        "end_date": "2020-01-03",
        "reports": [
            {"datetime": "2020-01-02 13:11:10.762", "bid": 4.0207, "ask": 4.0213},
            {"datetime": "2020-01-03 13:06:22.606", "bid": 4.0516, "ask": 4.0522},
        ],
    }

    assert historical_report.as_dict == expected


def test_historical_report_display(historical_report):
    expected = (
        "+-------------------------+--------+--------+\n"
        "| datetime                |    bid |    ask |\n"
        "|-------------------------+--------+--------|\n"
        "| 2020-01-02 13:11:10.762 | 4.0207 | 4.0213 |\n"
        "| 2020-01-03 13:06:22.606 | 4.0516 | 4.0522 |\n"
        "+-------------------------+--------+--------+"
    )

    assert historical_report.display() == expected
