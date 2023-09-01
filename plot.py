import pandas as pd
import matplotlib.pyplot as plt

import engine as e


def plot_chart(chart: dict):
    df = pd.DataFrame(chart['data'])
    df.plot(x='date', y='value', rot=0)
    plt.show()


def main():
    chart_id = input("Provide chart id: ")
    chart = e.get_chart_by_id(chart_id)
    plot_chart(chart)


if __name__ == '__main__':
    main()
