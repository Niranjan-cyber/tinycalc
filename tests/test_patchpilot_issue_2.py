import pytest
from tinycalc import mean

def test_mean_empty_raises_valueerror():
    with pytest.raises(ValueError):
        mean([])
