import json

import longscope.constants as c


def get_chart_by_id(chart_id: str) -> dict:
    """Returns chart find in 'charts' directory by its id."""
    with open(f'{c.CHARTS_DIRECTORY}/{chart_id}.json', 'r', encoding='utf-8') as f:
        chart = json.load(f)
    return chart


def get_charts_meta() -> dict:
    """Returns charts metadata from 'meta' directory."""
    with open(f'{c.META_DIRECTORY}/charts_meta.json', 'r') as f:
        charts_meta = json.load(f)
    return charts_meta


def write_chart_to_file(chart: dict):
    """Writes chart to the 'charts' directory."""
    with open(f'{c.CHARTS_DIRECTORY}/{chart["header"]["id"]}.json', 'w', encoding='utf-8') as f:
        json.dump(chart, f)
