import datetime as dt
import logging

from pocketbase import Client

from longscope.raw_data.nbp import NBP

logging.basicConfig(level=logging.INFO)


def main() -> None:
    nbp = NBP()
    client = Client('http://127.0.0.1:8090')
    client.admins.auth_with_password('test@test.com', 'dupa12345678')
    chart_data = nbp.get_data_for_code_and_date_range(table='a',
                                                      code='usd',
                                                      start_date='2002-01-02',
                                                      end_date=dt.date.today().strftime('%Y-%m-%d'))
    for record in chart_data:
        record_with_id = {'header_id': '2guodga73fv569i', **record.__dict__}
        client.collection('chart_data').create(record_with_id)


if __name__ == '__main__':
    main()
