import pytest
from pyhton_functions import addition


def test_addition():
    assert addition(1.0, 2.0) == 3.0
    assert addition(-1.0, 2.0) == 1.0
    assert addition(0.0, 0.0) == 0.0
