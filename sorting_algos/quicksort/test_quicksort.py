"""Test cases for quicksort."""

from .quicksort import quicksort, quicksort_helper, partition
import pytest

@pytest.fixture
def simple_arr():
    return [-1, 99, 35, 43, 5, 0, 40]


def test_quicksort_true(simple_arr):
    assert quicksort(simple_arr) == [-1, 0, 5, 35, 40, 43, 99]
