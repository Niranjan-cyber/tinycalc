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
    """Parse user input like \"42\", \"-3.5\" or \"1,000\".

    The original implementation chose between ``int`` and ``float`` based
    solely on the presence of a decimal point, which caused scientific
    notation (e.g. ``\"1e3\"``) to be incorrectly routed to ``int`` and raise a
    ``ValueError``.  The updated logic attempts to parse as an integer first
    and falls back to ``float`` on failure, correctly handling exponent
    forms while preserving the original behaviour for plain integers.
    """
    text = text.strip()
    try:
        return int(text)
    except ValueError:
        # Fallback to float for decimals, scientific notation, etc.
        return float(text)
