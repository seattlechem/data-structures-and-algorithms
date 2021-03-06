"""Print level order test."""
from .print_level_order import print_level_order
import pytest


def test_print_level_order_true(small_tree):
    """Confirm if true for level order print."""
    result = print_level_order(small_tree)
    assert result == '5 \n 9 3 \n '


def test_level_print_large_tree(large_tree):
    """Confirm the result of level_order_print of large_tree."""
    result = print_level_order(large_tree)
    assert result == '12 \n 9 2 11 \n 1 3 99 \n 13 14 \n '


def test_type_error():
    """Confirm if error is thrown if input is not K-ary Tree."""
    with pytest.raises(TypeError) as err:
        print_level_order(34)
        assert err is 'Input must be K-ary Tree.'


def test_value_error():
    """Confirm if error is thrown if input is missing."""
    with pytest.raises(ValueError) as err:
        print_level_order()
        assert err is 'Input is missing.'
