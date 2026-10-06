import numpy as np

from famam.my_module import add_numbers, typed_function


def test_typed_function():
    assert not typed_function(np.zeros(10), "")


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0.5, 0.25) == 0.75
