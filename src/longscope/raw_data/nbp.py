import datetime as dt
import logging
from itertools import chain
from typing import Iterable

import requests

from .model import Rate

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
# logger.addHandler(handler)

API_URL = 'https://api.nbp.pl/api/exchangerates/rates'
DATE_RANGE_LIMIT = 367
DATE_FORMAT = '%Y-%m-%d'


class NBP:
    uuid = '836c00a8-92ac-44fd-98ac-09f974bb89fe'

    @staticmethod
    def get_data_for_code_and_date(table: str, code: str, date: str = 'today') -> Rate:
        """Returns a rate for the given code and date."""
        logger.info(f'Fetching data from NBP for: {table=}, {code=}, {date=}')
        url = f'{API_URL}/{table}/{code}/{date}/?format=json'
        res = requests.get(url)
        res.raise_for_status()
        body = res.json()
        return NBP._response_to_rate(body['rates'][0]['mid'])

    @staticmethod
    def get_data_for_code_and_date_range(table: str, code: str, start_date: str, end_date: str) -> Iterable[Rate]:
        """Returns a rate list for the given code and date range."""
        n_days = (dt.date.fromisoformat(end_date) -
                  dt.date.fromisoformat(start_date)).days
        if n_days <= DATE_RANGE_LIMIT:
            logger.info(f'Fetching data from NBP for: {table=}, {code=}, {start_date=}, {end_date=}')
            url = f'{API_URL}/{table}/{code}/{start_date}/{end_date}/?format=json'
            res = requests.get(url)
            res.raise_for_status()
            body = res.json()
            return map(NBP._response_to_rate, body['rates'])

        limit_end_date = (dt.date.fromisoformat(start_date) + dt.timedelta(days=DATE_RANGE_LIMIT)).strftime(DATE_FORMAT)
        limit_start_date = (dt.date.fromisoformat(limit_end_date) + dt.timedelta(days=1)).strftime(DATE_FORMAT)
        return chain(NBP.get_data_for_code_and_date_range(table, code, start_date, limit_end_date),
                     NBP.get_data_for_code_and_date_range(table, code, limit_start_date, end_date))

    @staticmethod
    def _response_to_rate(response: dict) -> Rate:
        return Rate(time=response['effectiveDate'], value=response['mid'])
