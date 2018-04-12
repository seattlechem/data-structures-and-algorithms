from .towers_of_hanoi import towers_of_hanoi


def test_hanoi_three():
    assert towers_of_hanoi(3) == 'Disk 1 moved from A to C'
