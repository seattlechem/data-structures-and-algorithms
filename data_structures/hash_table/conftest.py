"""Create fixtures."""
import pytest


@pytest.fixture
def small_string():
    """Create small string only with space."""
    small_string = 'Lorem ipsum dolor sit amet consectetur adipiscing elit Nam \
    pretium orci sit amet tempor dapibus Interdum et malesuada fames ac ante \
    ipsum primis in faucibus Nam sit amet aliquet dui'
    return small_string
