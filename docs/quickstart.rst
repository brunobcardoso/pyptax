Quickstart
==========

Closing Ptax rates for a requested date
---------------------------------------

As a simple example, we'll request closing Ptax rates on January 20, 2020.
We have to inform the date in the format YYYY-MM-DD.

    >>> from pyptax import ptax
    >>> close_report = ptax.close('2020-01-20')
    >>> close_report
    CloseReport(datetime='2020-01-20 13:09:02.871', bid=4.1823, ask=4.1829)

The ptax.close returns an instance of CloseReport:

    >>> close_report.datetime
    '2020-01-20 13:09:02.871'
    >>> close_report.bid
    4.1823
    >>> close_report.ask
    4.1829

It's also possible to process the information as a dictionary:

    >>> close_report.as_dict
    {'datetime': '2020-01-20 13:09:02.871', 'bid': 4.1823, 'ask': 4.1829}

Or as a fixed width table for pretty printing:

    >>> print(close_report.display())
    +----------+-------------------------+
    | datetime | 2020-01-20 13:09:02.871 |
    | bid      | 4.1823                  |
    | ask      | 4.1829                  |
    +----------+-------------------------+

Historical Ptax rates for a requested period
--------------------------------------------

    >>> from pyptax import ptax
    >>> historical_report = ptax.historical('2020-01-01', '2020-01-05')
    >>> historical_report
    HistoricalReport(
        start_date="2020-01-01",
        end_date="2020-01-03",
        reports=[
            CloseReport("2020-01-02 13:11:10.762", 4.0207, 4.0213),
            CloseReport("2020-01-03 13:06:22.606", 4.0516, 4.0522),
        ],
    )

The ptax.historical returns an instance of HistoricalReport:

    >>> historical_report.start_date
    "2020-01-01"
    >>> historical_report.end_date
    "2020-01-03"
    >>> historical_report.reports
    [
        CloseReport("2020-01-02 13:11:10.762", 4.0207, 4.0213),
        CloseReport("2020-01-03 13:06:22.606", 4.0516, 4.0522),
    ]

As a dictionary:

    >>> historical_report.as_dict
    {
        "start_date": "2020-01-01",
        "end_date": "2020-01-03",
        "reports": [
            {"datetime": "2020-01-02 13:11:10.762", "bid": 4.0207, "ask": 4.0213},
            {"datetime": "2020-01-03 13:06:22.606", "bid": 4.0516, "ask": 4.0522},
        ],
    }

Or a as a fixed width table:

    >>> print(historical_report.display())
    +-------------------------+--------+--------+
    | datetime                |    bid |    ask |
    |-------------------------+--------+--------|
    | 2020-01-02 13:11:10.762 | 4.0207 | 4.0213 |
    | 2020-01-03 13:06:22.606 | 4.0516 | 4.0522 |
    +-------------------------+--------+--------+
