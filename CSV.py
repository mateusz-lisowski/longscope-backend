import json
import csv


with open('charts_meta.json', 'r') as f:
    charts_data = json.load(f)

for chart_meta in charts_data:

    data = []

    with open(f'data/{chart_meta["chart-id"]}.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:

            record = {
                'date': row[0],
                'value': float(row[1])
            }

            data.append(record)

    with open(f'charts/{chart_meta["chart-id"]}.json', 'r') as f:
        chart = json.load(f)

    chart["data"] = data

    with open(f'charts/{chart_meta["chart-id"]}.json', 'w') as f:
        json.dump(chart, f)
