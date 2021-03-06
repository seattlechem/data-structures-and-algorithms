"""HashTable test cases."""
from .hash_table import HashTable
import pytest


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


def test_hashtable_size():
    """Hashtable default size."""
    hashe = HashTable()
    assert hashe.max_size == 1024


def test_custom_hashtable_size():
    """Hashtable custom max size."""
    hashe = HashTable(33)
    assert hashe.max_size == 33


def test_remove_key_not_string():
    """Remove with no string key."""
    hashe = HashTable()
    with pytest.raises(TypeError) as err:
        hashe.remove(123)
        assert err.value == 'key must be string.'
