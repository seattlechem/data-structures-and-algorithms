"""Mergesort test cases."""
import pytest
from .mergesort import mergesort


@pytest.fixture
def nine_list():
    """Create nine element test list."""
    return [34, 19, 42, -9, 2018, 0, 2005, 77, 2099]


def test_nine_mbr_list_mergesort(nine_list):
    """Check if true for mergesort."""
    assert mergesort(nine_list) == [-9, 0, 19, 34, 42, 77, 2005, 2018, 2099]


def test_empty_list():
    """Check if empty list returns empty list."""
    ls = list()
    assert mergesort(ls) == []


def test_type_error_for_input():
    """Check if input is a list type."""
    with pytest.raises(TypeError) as err:
        mergesort(123)
        assert err == 'Input must be a list type.'


def test_all_elements_integer():
    """Check if all elements are integer."""
    with pytest.raises(TypeError) as err:
        ls = [1, 2, 3, 'a', 'b', 8]
        mergesort(ls)
        assert err == 'All elements must be an integer.'


def test_all_negative_num():
    """Check mergesort on all negative numbers."""
    ls = [-3, -66, -100, -125, -43, -25]
    assert mergesort(ls) == [-125, -100, -66, -43, -25, -3]
