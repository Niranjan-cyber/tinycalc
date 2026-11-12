"""Summary statistics used by the tinycalc CLI."""


def median(values):
    """Middle value of `values`; the mean of the two middle values for an even count."""
    s = sorted(values)
    if not s:
        raise ValueError("median() of an empty list")
    mid = len(s) // 2
    if len(s) % 2:
        return s[mid]
    return (s[mid] + s[mid + 1]) / 2
