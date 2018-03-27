import pytest
from largest_product import largest_product


def test_largest_product_array():
    assert largest_product([[1, 2], [3, 4], [5, 6], [7, 8]]) == 56


def test_largest_product_empty():
    assert largest_product([]) == 0


def test_largest_product_true():
    with pytest.raises(TypeError):
        largest_product([['a', 'b'], ['c', 'd']])


def test_single_element():
    assert largest_product([[1], [2], [3]]) == 6
