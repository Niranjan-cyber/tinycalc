"""Money and percentage helpers used by the tinycalc CLI."""


def percent_change(old, new):
    """How much `new` differs from `old`, in percent (50 -> 75 is +50.0)."""
    return (new - old) / new * 100


def apply_discount(price, percent):
    return round(price * (1 - percent / 100), 2)
