"""Fixtures."""
import pytest


@pytest.fixture
def small_string():
    """Fixture string."""
    a = 'apple grape scissor skiing apple grape scissor skiing'
    return a
