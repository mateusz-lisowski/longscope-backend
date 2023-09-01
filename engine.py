import json

import constants as c


def get_chart_by_id(chart_id: str) -> dict:
    with open(f'{c.CHARTS_DIRECTORY}/{chart_id}.json', 'r', encoding='utf-8') as f:
        chart = json.load(f)
    return chart


def write_chart_to_file(chart: dict):
    with open(f'{c.CHARTS_DIRECTORY}/{chart["header"]["id"]}.json', 'w', encoding='utf-8') as f:
        json.dump(chart, f)


def get_charts_meta():
    with open('charts_meta.json', 'r') as f:
        charts_meta = json.load(f)
    return charts_meta
