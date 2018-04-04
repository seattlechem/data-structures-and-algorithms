import pytest
from .fifo_animal_shelter import AnimalShelter
from .cat import Cat
from .dog import Dog


@pytest.fixture
def empty_animalshelter():
    return AnimalShelter()


def test_enqueue(empty_animalshelter):
    new_dog = Dog('dog1')
    dog_inserted = empty_animalshelter.enqueue(new_dog)
    assert type(dog_inserted.dequeue()) == 'Dog'
