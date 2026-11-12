import pytest
from tinycalc.ops import divide

def test_divide_by_zero_raises():
    """divide should raise ZeroDivisionError when divisor is zero."""
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
