from .client import Ptax
from .models import CloseReport
from .models import HistoricalReport
from .resources import CloseResource
from .resources import HistoricalResource


def close(date: str) -> CloseReport:
    """
    Retrieve closing Ptax rates on a certain date.

    Parameters
    ----------
    date
        Year, month and day of the date to be searched. Format - "YYYY-MM-DD"

    Returns
    -------
    CloseReport
        A CloseReport object with datetime, bid and ask attributes

    Raises
    ------
    DateFormatError
        If fails to parse the informed date

    Examples
    --------
    >>> close_report = close("2020-01-20")
    >>> close_report
    CloseReport(datetime=2020-01-20 13:09:02.871, bid=4.1823, ask=4.1829)
    >>> close_report.bid
    4.1823
    >>> close_report.ask
    4.1829
    >>> close_report.as_dict
    {'datetime': '2020-01-20 13:09:02.871', 'bid': 4.1823, 'ask': 4.1829}

    """
    resource = CloseResource(date)
    return Ptax(resource).response()


def historical(start_date: str, end_date: str) -> HistoricalReport:
    """
    Retrieve historical closing Ptax rates for the requested time period.

    Parameters
    ----------
    start_date
        Beginning of the time period to be searched. Format - 'YYYY-MM-DD'
    end_date
        End of the time period to be searched. Format - 'YYYY-MM-DD'

    Returns
    -------
    HistoricalReport
        A HistoricalReport object with start_date, end_date and reports with a list
        of CloseReports.

    Raises
    ------
    DateFormatError
        If fails to parse the informed date
    ClientError
        If Ptax Service response returns an error
    UnavailableDataError
        If receives an empty list from Ptax Service

    Examples
    --------
    >>> historical_report = historical("2020-01-02", "2020-01-03")
    >>> historical_report
    HistoricalReport(
        start_date="2020-01-02",
        end_date="2020-01-04",
        reports=[
            CloseReport(datetime="2020-01-02 13:11:10.762", bid=4.0207, ask=4.0213),
            CloseReport(datetime="2020-01-03 13:06:22.606", bid=4.0516, ask=4.0522),
        ],
    )
    >>> historical_report.as_dict
    {
        "start_date": "2020-01-02",
        "end_date": "2020-01-04",
        "reports": [
            {"datetime": "2020-01-02 13:11:10.762", "bid": 4.0207, "ask": 4.0213},
            {"datetime": "2020-01-03 13:06:22.606", "bid": 4.0516, "ask": 4.0522},
        ],
    }
    """
    resource = HistoricalResource(start_date, end_date)
    return Ptax(resource).response()
