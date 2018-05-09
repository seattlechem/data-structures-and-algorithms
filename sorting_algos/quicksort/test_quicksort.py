"""Test cases for quicksort."""

from .quicksort import quicksort
import pytest


@pytest.fixture
def simple_arr():
    """Create simple arr."""
    return [-1, 99, 35, 43, 5, 0, 40]


def test_quicksort_true(simple_arr):
    """True test case for quicksort."""
    assert quicksort(simple_arr) == [-1, 0, 5, 35, 40, 43, 99]


def test_type_err():
    """Confirm if type error is flagged."""
    ls = [-3, 'a', 'bd', 34, 100]
    with pytest.raises(TypeError) as err:
        quicksort(ls)
        assert err == 'All elements must be either an integer or string.'


def test_non_list():
    """Confirm if error is caught when passing non list parameter."""
    with pytest.raises(TypeError) as err:
        quicksort(123)
        assert err == 'Input must be a list type.'
