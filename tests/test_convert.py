from tinycalc.convert import km_to_miles


def test_km_to_miles():
    assert round(km_to_miles(10), 2) == 6.21
