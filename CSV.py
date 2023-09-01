import csv

import engine as e


def main():

    charts_meta = e.get_charts_meta()

    for chart_meta in charts_meta:

        data = []

        with open(f'data/{chart_meta["chart-id"]}.csv', 'r') as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:

                record = {
                    'date': row[0],
                    'value': float(row[1])
                }

                data.append(record)

        chart = e.get_chart_by_id(chart_meta["chart-id"])
        chart["data"] = data
        e.write_chart_to_file(chart)


if __name__ == '__main__':
    main()
