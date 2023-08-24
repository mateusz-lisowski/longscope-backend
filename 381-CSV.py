import datetime
import calendar
import csv

import pandas as pd
import matplotlib.pyplot as plt


chart_381 = {
    'header': {
            'id': 381,
            'name': 'Mieszkania oddane do użytkowania',
            'section': 16,
            'dimension': 2,
            'position': 33617,
            'periods': [247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258],
            'unit': 'sz.'
        },
    'data': []
}


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
    csv_to_chart_data('data/381-data.csv', chart_381)
    plot_chart(chart_381)


if __name__ == '__main__':
    main()
