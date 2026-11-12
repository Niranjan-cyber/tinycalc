from tinycalc.finance import percent_change


def test_percent_change_measured_against_old_value():
    # going from 50 to 75 is a 50% increase (change measured against the old value)
    assert percent_change(50, 75) == 50.0
    # going from 200 to 100 is a 50% decrease (measured against the old value)
    assert percent_change(200, 100) == -50.0
