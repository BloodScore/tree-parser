import re

from typing import Union

from src.parser.date_utils import parse_date, parse_term


def normalize_date(result: dict):
    for key, value in result.items():
        if isinstance(value, dict):
            normalize_date(value)

        if re.search(r'дата', key, re.IGNORECASE):
            result[key] = parse_date(value)


def normalize_term(result: dict):
    for key, value in result.items():
        if isinstance(value, dict):
            normalize_term(value)

        if re.search(r'срок', key, re.IGNORECASE):
            result[key] = parse_term(value)


def parse(trees: Union[list, dict]):
    result = {}

    if isinstance(trees, dict):
        trees = [trees]

    for tree in trees:
        for key, value in tree.items():
            if not result.get(key):
                result[key] = value
            else:
                temp_dict = result[key]
                temp_dict.update(value)

                result[key] = temp_dict

    normalize_date(result)
    normalize_term(result)

    return result
