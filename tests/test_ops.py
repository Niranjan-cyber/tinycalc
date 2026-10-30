import pytest

from tinycalc import add, divide, mean, parse_number, power, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_divide():
    assert divide(9, 3) == 3


def test_power():
    assert power(2, 10) == 1024


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5


def test_parse_simple():
    assert parse_number("42") == 42
    assert parse_number(" -3.5 ") == -3.5
