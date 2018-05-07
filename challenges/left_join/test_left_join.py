"""."""

import pytest
from .hash_table import HashTable as HT
from .left_join import left_join


def test_left_join_true(six_key_ht, five_key_ht):
    """True case for left join."""
    result = left_join(six_key_ht, five_key_ht)
    assert result.get('cost') == (0, None)


def test_both_empty_hash_table():
    """Result when both inputs are empty HashTable."""
    hash1 = HT()
    hash2 = HT()

    result = left_join(hash1, hash2)
    for i in range(0, 1023):
        assert result.buckets[i]._len == 0


def test_value_error(five_key_ht):
    """Value error check."""
    with pytest.raises(ValueError) as err:
        left_join(five_key_ht)
        assert err == 'At least one input must be HashTable'


def test_type_error_one(six_key_ht):
    """Type Error check when only one input is not HashTable."""
    with pytest.raises(TypeError) as err:
        left_join(six_key_ht, 15)
        assert err == 'Input must be HashTable.'
