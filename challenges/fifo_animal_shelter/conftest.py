from .dog import Dog
from .cat import Cat
from .fifo_animal_shelter import AnimalShelter
import pytest


@pytest.fixture
def empty_animalshelter():
    return AnimalShelter()
