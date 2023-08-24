import datetime
import calendar
import csv

import pandas as pd
import matplotlib.pyplot as plt

PERIODS = {
    'year': 282,
    'q1': 270,
    'q2': 271,
    'q3': 272,
    'q4': 273,
    'm1': 111,
}

CHART_469 = {
    'header': {

    },
    'data': [
        {
            'date': None,
            'value': None,
        },
        {
            'date': None,
            'value': None,
        },
    ]
}

BWUK = {
    'id': 469,
    'name': 'Bierzący wskaźnik ufności konsumenckiej (BWUK)',
    'section': 16,
    'dimension': 2,
    'position': 33617,
    'periods': [247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258],
    'unit': 'PLN'
}

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

with open('data/381-data.csv', 'r') as f:
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

        chart_381['data'].append(record)

df = pd.DataFrame(chart_381['data'])
df.plot(x='date', y='value', rot=0)
plt.show()


# def main():
#
#     # while True:
#     #     current_date = datetime.datetime
print(f'''https://api-dbw.stat.gov.pl/api/1.1.0/variable/variable-data-section?id-zmienna={BWUK['id']}&id-przekroj={BWUK['section']}&id-rok=2023&id-okres={BWUK['periods'][0]}&ile-na-stronie=5000&numer-strony=0&lang=pl''')
#     # print(req.url)
#     # rich.print(req.json()['data'][0])
#
#
# if __name__ == '__main__':
#     main()
