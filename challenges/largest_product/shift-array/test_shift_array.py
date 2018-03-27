from shift_array import insertShiftArray


def test_insert_shift_array():
    assert insertShiftArray([2, 4, 6, 8], 5) == [2, 4, 5, 6, 8]
