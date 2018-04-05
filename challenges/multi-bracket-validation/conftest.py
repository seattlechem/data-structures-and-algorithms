import pytest


@pytest.fixture
def small_false_string():
    return "\{\}{{{[][](())"


@pytest.fixture
def square_true_string():
    return '[][][][][]'


@pytest.fixture
def mixed_square_true_string():
    return 'a[b]c[dd[ee]]f[g]'
