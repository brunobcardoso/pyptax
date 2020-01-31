from .helpers import DateParser
from .models import CloseReport
from .models import HistoricalReport
from pyptax import settings
from pyptax.exceptions import UnavailableDataError


class CloseResource:
    path = settings.CLOSE_RESOURCE

    def __init__(self, date):
        self.date = date
        self.parsed_date = DateParser(date).parse()

    @property
    def params(self):
        return f"@dataCotacao={self.parsed_date!r}&$format=json"

    def parse(self, raw_data):
        try:
            data = raw_data["value"][0]
        except IndexError:
            raise UnavailableDataError(
                f"Unavailable rates for the requested date:{self.date!r}"
            )
        datetime = data["dataHoraCotacao"]
        bid = data["cotacaoCompra"]
        ask = data["cotacaoVenda"]
        return CloseReport(datetime, bid, ask)


class HistoricalResource:
    path = settings.HISTORICAL_RESOURCE

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.parsed_start = DateParser(start_date).parse()
        self.parsed_end = DateParser(end_date).parse()

    @property
    def params(self):
        return f"@dataInicial={self.parsed_start!r}&@dataFinalCotacao={self.parsed_end!r}&$format=json"

    def parse(self, raw_data):
        reports_list = raw_data["value"]
        if not reports_list:
            raise UnavailableDataError(
                f"Unavailable rates for the requested range: {self.start_date!r} - {self.end_date!r}"
            )

        close_reports = [
            CloseReport(
                report["dataHoraCotacao"],
                report["cotacaoCompra"],
                report["cotacaoVenda"],
            )
            for report in reports_list
        ]

        return HistoricalReport(self.start_date, self.end_date, close_reports)
