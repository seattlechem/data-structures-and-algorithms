"""Repeated word test."""
import pytest
from .repeated_word import repeated_word


def test_repeated_word_true(small_string):
    """Compare the first occurrance of word repeated more than once."""
    result = repeated_word(small_string)
    assert result == 'apple'


def test_empty_string():
    """Value error check."""
    with pytest.raises(ValueError):
        repeated_word('')


def test_type_error():
    """Type error check."""
    with pytest.raises(TypeError):
        repeated_word(123)
