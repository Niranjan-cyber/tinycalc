from tinycalc import parse_number


def test_parse_number_with_comma():
    assert parse_number("1,000") == 1000
