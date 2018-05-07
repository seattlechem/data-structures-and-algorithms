"""Merge sort function."""
import math


def mergesort(ls):
    """Divide the list into two pieces."""
    if len(ls) == 1:
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
            results.append(left.shift())
        else:
            results.append(right.shift())
    return [results[::], left[::], right[::]]
