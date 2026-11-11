from tinycalc.finance import apply_discount, percent_change


def test_no_change():
    assert percent_change(100, 100) == 0


def test_discount():
    assert apply_discount(80, 25) == 60
