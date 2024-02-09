import re
import dateparser

from datetime import datetime


def parse_date(value: str) -> str:
    normalized = dateparser.parse(value)

    try:
        return normalized.strftime('%d.%m.%Y')
    except Exception:
        return value


def parse_term(value: str) -> str:
    normalized = dateparser.parse(value)

    if not normalized:
        if re.search(r'\d+ [^ 0-9]+', value):
            normalized = dateparser.parse(re.search(r'\d+ [^ 0-9]+', value).group(0))

    try:
        term = datetime.now() - normalized

        days = abs(term.days)

        years = days // 365
        months = (days % 365) // 30
        weeks = ((days % 365) % 30) // 7
        days = (((days % 365) % 30) % 7)

        return f'{years}_{months}_{weeks}_{days}'
    except Exception:
        return value
