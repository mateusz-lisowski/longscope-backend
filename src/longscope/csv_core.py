import csv

import longscope.engine as e


def get_csv_reader(chart_id: str) -> csv.reader:
    """Function for returning csv reader from the file."""

    with open(f'data/{chart_id}.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
    return csv_reader


# Main function of the program
def main():

    # Get charts metadata
    charts_meta = e.get_charts_meta()

    # Iterate through them
    for chart_meta in charts_meta:

        data = []
        chart = e.get_chart_by_id(chart_meta["chart-id"])

        # Add charts data from the csv file
        csv_reader = get_csv_reader(chart_meta["chart-id"])
        for row in csv_reader:

            record = {
                'date': row[0],
                'value': float(row[1])
            }

            data.append(record)

        # Replace old data and write complete chart to the file
        chart["data"] = data
        e.write_chart_to_file(chart)


if __name__ == '__main__':
    main()
