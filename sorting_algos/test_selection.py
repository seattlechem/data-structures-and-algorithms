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
