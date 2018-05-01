"""Repeated word test."""
import pytest
from .repeated_word import repeated_word


@pytest.fixture
def small_string():
    """Fixture string."""
    a = 'apple grape scissor skiing apple grape scissor skiing'
    return a


def test_repeated_word_true(small_string):
    """Compare the first occurrance of word repeated more than once."""
    result = repeated_word(small_string)
    assert result == 'apple'
