"""Small arithmetic helpers used by the tinycalc CLI."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0


def power(a, b):
    return a ** b


def mean(values):
    values = list(values)
    if not values:
        return 0
    return sum(values) / len(values)


def parse_number(text):
    """Parse user input like "42", "-3.5" or "1,000".

    Removes commas used as thousands separators before converting.
    """
    # Strip whitespace and remove comma separators
    cleaned = text.strip().replace(",", "")
    # Use float for numbers containing a decimal point, otherwise int
    return float(cleaned) if "." in cleaned else int(cleaned)
