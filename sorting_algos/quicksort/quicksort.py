"""Quick sort function."""


def quicksort(arr):
    """."""
    quicksort_helper(arr, 0, len(arr) - 1)


def quicksort_helper(arr, first, last):
    """."""
    if first < last:
        split_point = partition(arr, first, last)
        quicksort_helper(arr, first, split_point - 1)
        quicksort_helper(arr, split_point + 1, last)


def partition(arr, first, last):
    """."""
    pivot_val = arr[first]
    leftmark = first + 1
    rightmark = last

    done = False

    while not done:
        
