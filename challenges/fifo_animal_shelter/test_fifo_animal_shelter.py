import pytest
from .fifo_animal_shelter import AnimalShelter
from .cat import Cat
from .dog import Dog


@pytest.fixture
def empty_animalshelter():
    return AnimalShelter()


def test_enqueue(empty_animalshelter):
    new_dog = Dog('dog1')
    # import pdb; pdb.set_trace()
    empty_animalshelter.enqueue(new_dog)
    empty_animalshelter.enqueue(new_dog)
    assert type(empty_animalshelter.dequeue('Dog')) == 'Dog'
