def test_base_as_dict(bulletin):
    expected = {
        "datetime": "2019-01-25 12:21",
        "bid": 4.3565,
        "ask": 4.3574,
        "bulletin_type": "close",
    }
    assert bulletin.as_dict == expected


def test_base_display(historical_bulletin):
    expected = (
        "+-------------------------+--------+--------+-----------------+\n"
        "| datetime                |    bid |    ask | bulletin_type   |\n"
        "|-------------------------+--------+--------+-----------------|\n"
        "| 2020-01-02 13:11:10.762 | 4.0207 | 4.0213 | close           |\n"
        "| 2020-01-03 13:06:22.606 | 4.0516 | 4.0522 | close           |\n"
        "+-------------------------+--------+--------+-----------------+"
    )

    assert historical_bulletin.display() == expected


def test_bulletin_display(bulletin):
    expected = (
        "+---------------+------------------+\n"
        "| datetime      | 2019-01-25 12:21 |\n"
        "| bid           | 4.3565           |\n"
        "| ask           | 4.3574           |\n"
        "| bulletin_type | close            |\n"
        "+---------------+------------------+"
    )
    assert bulletin.display() == expected
