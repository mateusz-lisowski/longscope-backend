import datetime
import time
import calendar

import requests
import pandas as pd
import matplotlib.pyplot as plt


chart_381 = {
    'header': {
            'id': 381,
            'name': 'Mieszkania oddane do użytkowania',
            'section': 16,
            'dimension': 2,
            'position': 33617,
            'periods': (247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258),
            'unit': 'sz.'
        },
    'data': []
}


current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month - 2

while True:

    req_url = (
        'https://api-dbw.stat.gov.pl/api/1.1.0/variable/variable-data-section'
        f'?id-zmienna={chart_381["header"]["id"]}'
        f'&id-przekroj={chart_381["header"]["section"]}'
        f'&id-rok={current_year}'
        f'&id-okres={chart_381["header"]["periods"][current_month - 1]}'
        '&ile-na-stronie=5000'
        '&numer-strony=0'
        '&lang=pl'
    )

    req = requests.get(req_url)
    time.sleep(9)

    try:
        data = req.json()['data']
    except KeyError:
        break

    for row in data:
        days = calendar.monthrange(current_year, current_month)[1]
        date = datetime.datetime(current_year, current_month, days)

        if (row['id-wymiar-1'] == chart_381["header"]["dimension"]
                and row['id-pozycja-1'] == chart_381["header"]["position"]):
            record = {
                'date': date.strftime('%Y-%m-%d'),
                'value': row['wartosc']
            }
            chart_381['data'].insert(0, record)

    current_month -= 1
    if current_month <= 0:
        current_year -= 1
        current_month = 12

    # Safety switch
    # if current_year <= 2020:
    #     break


df = pd.DataFrame(chart_381['data'])
df.plot(x='date', y='value', rot=0)
plt.show()
