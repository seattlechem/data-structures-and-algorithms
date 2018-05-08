"""Merge sort function."""
import math


def mergesort(ls):
    """Divide the list into two pieces."""
    if type(ls) is not list:
        raise TypeError('Input must be a list type.')

    for i in range(1, len(ls)):
        if not isinstance(ls[i], int):
            raise TypeError('All elements must be an integer.')

    if len(ls) <= 1:
        return ls

    center = math.floor(len(ls) / 2)
    left = ls[0:center]
    right = ls[center:]

    return merge(mergesort(left), mergesort(right))


def merge(left, right):
    """Two lists are merged."""
    results = []

    while len(left) and len(right):
        if left[0] < right[0]:
            results.append(left.pop(0))
        else:
            results.append(right.pop(0))
    return results + left + right
