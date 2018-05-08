"""Selection sort test cases."""
import pytest
from .selection import selection


@pytest.fixture
def simple_unordered_list():
    """Create a simple unordered list."""
    return [15, 7, 77, 128, -5, 0]


def test_selection(simple_unordered_list):
    """Confirm if simple unordered list is sorted by selection."""
    result = selection(simple_unordered_list)
    assert result == [-5, 0, 7, 15, 77, 128]


def test_type_err():
    """Confirm if type error is flagged."""
    ls = [-3, 'a', 'bd', 34, 100]
    with pytest.raises(TypeError) as err:
        selection(ls)
        assert err == 'All elements must be either an integer or string.'
