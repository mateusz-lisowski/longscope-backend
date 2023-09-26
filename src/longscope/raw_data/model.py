from dataclasses import dataclass
from typing import Iterable, Protocol


@dataclass
class Rate:
    time: str
    value: float


class DataFetcher(Protocol):
    uuid: str

    @staticmethod
    def get_data_for_code_and_date(table: str, code: str, date: str = 'today') -> Rate:
        """Returns a rate for the given code and date."""

    @staticmethod
    def get_data_for_code_and_date_range(table: str, code: str, start_date: str, end_date: str) -> Iterable[Rate]:
        """Returns a rate list for the given code and date range."""
