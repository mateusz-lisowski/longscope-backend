import json

import pandas as pd
import matplotlib.pyplot as plt


def get_chart_by_id(chart_id: str) -> dict:
    with open(f'charts/{chart_id}.json', 'r') as f:
        chart = json.load(f)

    return chart


def plot_chart(chart: dict):
    df = pd.DataFrame(chart['data'])
    df.plot(x='date', y='value', rot=0)
    plt.show()


def main():
    chart_id = input("Provide chart id: ")
    chart = get_chart_by_id(chart_id)
    plot_chart(chart)


if __name__ == '__main__':
    main()
