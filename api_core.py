# Importing build-in modules
import datetime
import time
import calendar
from dateutil.relativedelta import relativedelta

# Importing third party modules
import requests

# Import project modules
import engine as e


def get_data_dbw_monthly(chart_id: str, url: str):

    # Get chart and its data
    chart = e.get_chart_by_id(chart_id)
    chart_data: list[dict] = chart["data"]

    # Calculate dates
    date_as_string = chart["data"][-1]["date"]
    last_date = datetime.date(*map(int, date_as_string.split('-')))
    next_date = last_date + relativedelta(months=1)

    # Send request till there are no more recent data
    while next_date <= datetime.datetime.now().date():

        # Send a request
        req_url = f'{url}&id-rok={next_date.year}&id-okres={(lambda x: x + 246)(next_date.month)}'
        response = requests.get(req_url)

        # If there is no data - break
        if response.status_code != 200:
            break

        # We take first record in the data list
        data = response.json()["data"][0]

        # Write new record to the chart's data list
        date_to_write = datetime.date(
            next_date.year,
            next_date.month,
            calendar.monthrange(next_date.year, next_date.month)[1]
        )

        record = {
            'date': date_to_write.strftime('%Y-%m-%d'),
            'value': data["wartosc"]
        }

        chart_data.append(record)

        # Wait in order for not to overflow DBW servers
        time.sleep(0.2)

        # Change date to the next month
        next_date = next_date + relativedelta(months=1)

    e.write_chart_to_file(chart)


def main():

    charts_meta = e.get_charts_meta()

    for chart_meta in charts_meta:

        # DBW API
        if chart_meta["api-id"] == "1f0a88c6-3e78-4231-8fb2-706ba63ff53b":

            url = chart_meta["url"]
            chart_id = chart_meta["chart-id"]
            current_year = datetime.datetime.now().year

            req_month = f'{url}&id-rok={current_year - 2}&id-okres=258'
            req_quarter = f'{url}&id-rok={current_year - 2}&id-okres=273'
            req_year = f'{url}&id-rok={current_year - 2}&id-okres=282'

            if requests.get(req_month).status_code == 200:
                print("Type of downloading: month")
                get_data_dbw_monthly(chart_id, url)
            elif requests.get(req_quarter).status_code == 200:
                print("Type of downloading: quarter")
            elif requests.get(req_year).status_code == 200:
                print("Type of downloading: year")


if __name__ == '__main__':
    main()
