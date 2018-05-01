import pytest
from .repeated_word import repeated_word


@pytest.fixture
def small_string():
    a = 'apple grape scissor skiing apple grape scissor skiing'
    return a


def test_repeated_word_true(small_string):
    result = repeated_word(small_string)
    import pdb; pdb.set_trace()
    assert result == 'apple'
