"""HashTable test cases."""
from .hash_table import HashTable
import pytest
# from .linked_list import LinkedList as LL


def test_small_string_find(small_string):
    """Small string is tested to see if a certain word can be found."""
    hashe = HashTable(1024)
    hashe.set(small_string, small_string)
    assert hashe.get(small_string) == small_string


def test_max_limit_type_err():
    """When making an instance with string."""
    with pytest.raises(TypeError):
        HashTable('test')


def test_hash_key_type_err():
    """When making an hash key with integer."""
    with pytest.raises(TypeError):
        hashe = HashTable()
        hashe.hash_key(123)


def test_set(small_string):
    """Confirm if value is inserted."""
    hashe = HashTable()
    hashe.set(small_string, 12)
    assert len(hashe.buckets[hashe.hash_key(small_string)]) == 1


def test_get(small_string):
    """Confirm the get method."""
    hashe = HashTable()
    hashe.set(small_string, 12)
    assert hashe.get(small_string) == 12


def test_remove(small_string):
    """Confirm the remove method."""
    hashe = HashTable()
    hashe.set(small_string, 256)
    assert hashe.get(small_string) == 256
    hashe.remove(small_string)
    assert hashe.buckets[hashe.hash_key(small_string)] is None
