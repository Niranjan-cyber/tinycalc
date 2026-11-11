import pytest

from tinycalc import parse_number


def test_parse_scientific_notation_lowercase():
    assert parse_number("1e3") == 1000.0


def test_parse_scientific_notation_uppercase_negative_exponent():
    assert parse_number("2E-2") == 0.02


@pytest.mark.parametrize(
    "text,expected",
    [
        ("1e3", 1000.0),
        ("2E-2", 0.02),
        ("1e0", 1.0),
        ("5E+1", 50.0),
    ],
)
def test_scientific_notation_is_valid_numeric_input(text, expected):
    assert parse_number(text) == expected
