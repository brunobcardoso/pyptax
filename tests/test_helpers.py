import pytest

from pyptax.helpers import BulletinTypeParser, DateFormatError, DateParser


def test_date_parser_parse_dafault():
    assert DateParser("2020-01-02").parse() == "01-02-2020"


@pytest.mark.parametrize("date", ("02/01/2020", "02-01-2020"))
def test_date_parser_parse_error(date):
    with pytest.raises(
        DateFormatError, match=r". does not match the required format YYYY-MM-DD"
    ):
        DateParser(date).parse()


@pytest.mark.parametrize(
    "date, fmt, expected_result",
    (
        ("2020-01-02", "%m-%d-%Y", "01-02-2020"),
        ("2020-01-02", "%d/%m/%Y", "02/01/2020"),
    ),
)
def test_date_parser_parse_change_format(date, fmt, expected_result):
    assert DateParser(date).parse(fmt) == expected_result


@pytest.mark.parametrize(
    "bulletin_type, expected_result",
    (
        ("Abertura", "open"),
        ("Intermediário", "intermediary"),
        ("Fechamento PTAX", "close"),
    ),
)
def test_bulletin_type_parser(bulletin_type, expected_result):
    assert BulletinTypeParser(bulletin_type).parse() == expected_result
