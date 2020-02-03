from unittest import mock

import pytest
from click.testing import CliRunner

import pyptax
from pyptax.cli import cli
from pyptax.exceptions import ClientError


@pytest.fixture
def cli_runner():
    return CliRunner()


def test_version(cli_runner):
    result = cli_runner.invoke(cli, ["--version"])

    assert pyptax.__version__ in result.output
    assert result.exit_code == 0


def test_no_subcommand_shows_help_message(cli_runner):
    result = cli_runner.invoke(cli)

    assert "PyPtax Command Line Interface" in result.output
    assert result.exit_code == 0


@mock.patch("pyptax.ptax.close", autospec=True)
def test_close(mock_close, cli_runner):
    date = "2020-01-20"

    result = cli_runner.invoke(cli, ["close", "--date", date])

    mock_close.assert_called_once_with(date)
    assert result.exit_code == 0


@mock.patch("pyptax.ptax.close", autospec=True)
def test_close_error(mock_close, cli_runner):
    date = "2020-01-20"
    expected = "Test Error"
    mock_close.side_effect = ClientError(expected)

    result = cli_runner.invoke(cli, ["close", "--date", date])

    mock_close.assert_called_once_with(date)
    assert expected in result.output
    assert result.exit_code == 0


@mock.patch("pyptax.ptax.historical", autospec=True)
def test_historical(mock_historical, cli_runner):
    start_date = "2020-01-01"
    end_date = "2020-01-03"

    result = cli_runner.invoke(
        cli, ["historical", "--start_date", start_date, "--end_date", end_date]
    )

    mock_historical.assert_called_once_with(start_date, end_date)
    assert result.exit_code == 0


@mock.patch("pyptax.ptax.historical", autospec=True)
def test_historical_error(mock_historical, cli_runner):
    start_date = "2020-01-01"
    end_date = "2020-01-03"
    expected = "Test Error"
    mock_historical.side_effect = ClientError(expected)

    result = cli_runner.invoke(
        cli, ["historical", "--start_date", start_date, "--end_date", end_date]
    )

    mock_historical.assert_called_once_with(start_date, end_date)
    assert expected in result.output
    assert result.exit_code == 0


@mock.patch("pyptax.ptax.intermediary", autospec=True)
def test_intermediary(mock_intermediary, cli_runner):
    date = "2020-01-02"

    result = cli_runner.invoke(cli, ["intermediary", "--date", date])

    mock_intermediary.assert_called_once_with(date)
    assert result.exit_code == 0


@mock.patch("pyptax.ptax.intermediary", autospec=True)
def test_intermediary_error(mock_intermediary, cli_runner):
    date = "2020-01-01"
    expected = "Test Error"
    mock_intermediary.side_effect = ClientError(expected)

    result = cli_runner.invoke(cli, ["intermediary", "--date", date])

    mock_intermediary.assert_called_once_with(date)
    assert expected in result.output
    assert result.exit_code == 0
