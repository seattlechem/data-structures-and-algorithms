import pytest


@pytest.fixture
def small_false_string():
    return "\{\}{{{[][](())"
