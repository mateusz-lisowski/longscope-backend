import datetime
import calendar
import csv
import json

import pandas as pd
import matplotlib.pyplot as plt


def get_chart_by_id(path: str, chart_id: int) -> dict:
    with open(path, 'r') as f:
        charts = json.load(f)
        for chart in charts:
            if chart['header']['id'] == chart_id:
                return chart


def csv_to_chart_data(path: str, chart: dict):
    with open(path, 'r') as f:

        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:

            year, month, value = row

            year = int(year)
            month = int(month)
            value = int(value)

            days = calendar.monthrange(year, month)[1]
            date = datetime.datetime(year, month, days)

            record = {
                'date': date.strftime('%Y-%m-%d'),
                'value': value
            }

            chart['data'].append(record)


def plot_chart(chart: dict):
    df = pd.DataFrame(chart['data'])
    df.plot(x='date', y='value', rot=0)
    plt.show()


def main():
    chart_381 = get_chart_by_id('data/charts_config.json', 381)
    csv_to_chart_data('data/381-data.csv', chart_381)
    plot_chart(chart_381)


if __name__ == '__main__':
    main()
