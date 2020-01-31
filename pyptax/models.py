from dataclasses import asdict
from dataclasses import dataclass
from typing import List
from typing import Optional

from tabulate import tabulate


@dataclass
class CloseReport:
    datetime: str
    bid: float
    ask: float

    @property
    def as_dict(self):
        return asdict(self)

    def display(self, fmt: Optional[str] = "psql") -> str:
        return tabulate(self.as_dict.items(), tablefmt=fmt)


@dataclass
class HistoricalReport:
    start_date: str
    end_date: str
    reports: List[CloseReport]

    @property
    def as_dict(self):
        return asdict(self)

    def display(self, fmt: Optional[str] = "psql") -> str:
        rows = ((report.datetime, report.bid, report.ask) for report in self.reports)
        return tabulate(rows, headers=self.reports[0].as_dict.keys(), tablefmt=fmt)
