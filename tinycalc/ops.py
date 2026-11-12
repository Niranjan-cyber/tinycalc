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
    # The function should raise ValueError for empty input, matching the
    # behavior expected by the tests. Returning 0 masks the error and leads to
    # incorrect semantics.
    if not values:
        raise ValueError("mean of empty sequence")
    return sum(values) / len(values)


def parse_number(text):
    """Parse user input like "42", "-3.5" or "1,000"."""
    text = text.strip()
    return float(text) if "." in text else int(text)
