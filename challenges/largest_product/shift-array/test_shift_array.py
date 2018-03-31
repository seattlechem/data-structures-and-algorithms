from shift_array import insertShiftArray
import pytest


def test_insert_shift_array_pass():
    assert insertShiftArray([2, 4, 6, 8], 5) == [2, 4, 5, 6, 8]


def test_insert_shift_array_single_element_list():
    assert insertShiftArray([2, 3, 4], 5) == [2, 3, 5, 4]


def test_type_error():
    """when TypeError occurs"""
    with pytest.raises(TypeError):
        insertShiftArray('a', 'b')
