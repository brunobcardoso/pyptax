Quickstart
==========

Closing Ptax rates for a requested date
---------------------------------------

As a simple example, we'll request closing Ptax rates on January 20, 2020.
We have to inform the date in the format YYYY-MM-DD.

    >>> from pyptax import ptax
    >>> bulletin = ptax.close('2020-01-20')
    >>> bulletin
    Bulletin(
        datetime="2020-01-20 13:09:02.871",
        bid=4.1823,
        ask=4.1829,
        bulletin_type="close"
    )

The ptax.close returns an instance of Bulletin:

    >>> bulletin.datetime
    '2020-01-20 13:09:02.871'
    >>> bulletin.bid
    4.1823
    >>> bulletin.ask
    4.1829

It's also possible to process the information as a dictionary:

    >>> bulletin.as_dict
    {
        "datetime": "2020-01-20 13:09:02.871",
        "bid": 4.1823,
        "ask": 4.1829,
        "bulletin_type": "close"
    }

Or as a fixed width table for pretty printing:

    >>> print(bulletin.display())
    +---------------+-------------------------+
    | datetime      | 2020-01-20 13:09:02.871 |
    | bid           | 4.1823                  |
    | ask           | 4.1829                  |
    | bulletin_type | close                   |
    +---------------+-------------------------+

Historical Ptax rates for a requested period
--------------------------------------------

    >>> from pyptax import ptax
    >>> historical_bulletin = ptax.historical('2020-01-01', '2020-01-05')
    >>> historical_bulletin
    HistoricalBulletin(
        start_date="2020-01-01",
        end_date="2020-01-03",
        bulletins=[
            Bulletin("2020-01-02 13:11:10.762", 4.0207, 4.0213, "close"),
            Bulletin("2020-01-03 13:06:22.606", 4.0516, 4.0522, "close"),
        ],
    )

The ptax.historical returns an instance of HistoricalBulletin:

    >>> historical_bulletin.start_date
    "2020-01-01"
    >>> historical_bulletin.end_date
    "2020-01-03"
    >>> historical_bulletin.bulletins
    [
        Bulletin("2020-01-02 13:11:10.762", 4.0207, 4.0213, "close"),
        Bulletin("2020-01-03 13:06:22.606", 4.0516, 4.0522, "close"),
    ]

As a dictionary:

    >>> historical_bulletin.as_dict
    {
        "start_date": "2020-01-01",
        "end_date": "2020-01-03",
        "bulletins": [
            {
                "datetime": "2020-01-02 13:11:10.762",
                "bid": 4.0207,
                "ask": 4.0213,
                "bulletin_type": "close"
            },
            {
                "datetime": "2020-01-03 13:06:22.606",
                "bid": 4.0516,
                "ask": 4.0522,
                "bulletin_type": "close"
            },
        ],
    }

Or a as a fixed width table:

    >>> print(historical_bulletin.display())
    +-------------------------+--------+--------+-----------------+
    | datetime                |    bid |    ask | bulletin_type   |
    |-------------------------+--------+--------+-----------------|
    | 2020-01-02 13:11:10.762 | 4.0207 | 4.0213 | close           |
    | 2020-01-03 13:06:22.606 | 4.0516 | 4.0522 | close           |
    +-------------------------+--------+--------+-----------------+

Intermediary Ptax rates for a requested date
--------------------------------------------

    >>> from pyptax import ptax
    >>> intermediary = ptax.intermediary('2020-01-02')
    >>> intermediary
    IntermediaryBulletin(
        date='2020-01-02',
        bulletins=[
            Bulletin(
                datetime='2020-01-02 10:08:18.114',
                bid=4.0101,
                ask=4.0107,
                bulletin_type='open'
            ),
            Bulletin(
                datetime='2020-01-02 11:03:40.704',
                bid=4.0118,
                ask=4.0124,
                bulletin_type='intermediary'
            ),
            Bulletin(
                datetime='2020-01-02 12:10:55.168',
                bid=4.0302,
                ask=4.0308,
                bulletin_type='intermediary'
            ),
            Bulletin(
                datetime='2020-01-02 13:11:10.756',
                bid=4.0305,
                ask=4.0311,
                bulletin_type='intermediary'
            ),
            Bulletin(
                datetime='2020-01-02 13:11:10.762',
                bid=4.0207,
                ask=4.0213,
                bulletin_type='close'
            )
        ]
    )

The ptax.intermediary returns an instance of IntermediaryBulletin:

    >>> intermediary.date
    "2020-01-02"
    >>> intermediary.bulletins
    [
        Bulletin("2020-01-02 10:08:18.114", 4.0101, 4.0107, "open"),
        Bulletin("2020-01-02 11:03:40.704", 4.0118, 4.0124, "intermediary"),
        Bulletin("2020-01-02 12:10:55.168", 4.0302, 4.0308, "intermediary"),
        Bulletin("2020-01-02 13:11:10.756", 4.0305, 4.0311, "intermediary"),
        Bulletin("2020-01-02 13:11:10.762", 4.0207, 4.0213, "close"),
    ]

As a dictionary:

    >>> intermediary.as_dict
    {
        'date': '2020-01-02',
        'bulletins': [
            {
                'datetime': '2020-01-02 10:08:18.114',
                'bid': 4.0101,
                'ask': 4.0107,
                'bulletin_type': 'open'
            },
            {
                'datetime': '2020-01-02 11:03:40.704',
                'bid': 4.0118,
                'ask': 4.0124,
                'bulletin_type': 'intermediary'
            },
            {
                'datetime': '2020-01-02 12:10:55.168',
                'bid': 4.0302,
                'ask': 4.0308,
                'bulletin_type': 'intermediary'
            },
            {
                'datetime': '2020-01-02 13:11:10.756',
                'bid': 4.0305,
                'ask': 4.0311,
                'bulletin_type': 'intermediary'
            },
            {
                'datetime': '2020-01-02 13:11:10.762',
                'bid': 4.0207,
                'ask': 4.0213,
                'bulletin_type': 'close'
            }
        ]
    }

Or a as a fixed width table:

    >>> print(intermediary.display())
    +-------------------------+--------+--------+-----------------+
    | datetime                |    bid |    ask | bulletin_type   |
    |-------------------------+--------+--------+-----------------|
    | 2020-01-02 10:08:18.114 | 4.0101 | 4.0107 | open            |
    | 2020-01-02 11:03:40.704 | 4.0118 | 4.0124 | intermediary    |
    | 2020-01-02 12:10:55.168 | 4.0302 | 4.0308 | intermediary    |
    | 2020-01-02 13:11:10.756 | 4.0305 | 4.0311 | intermediary    |
    | 2020-01-02 13:11:10.762 | 4.0207 | 4.0213 | close           |
    +-------------------------+--------+--------+-----------------+
