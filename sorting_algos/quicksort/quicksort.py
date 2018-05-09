"""Quick sort function."""


def quicksort(arr):
    """."""
    # import pdb; pdb.set_trace()
    quicksort_helper(arr, 0, len(arr) - 1)
    return arr


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
        while leftmark <= rightmark and arr[leftmark] <= pivot_val:
            # print(f'first while: lm{leftmark}, rm{rightmark}, {arr[leftmark]}, {pivot_val}')
            leftmark += 1

        while arr[rightmark] >= pivot_val and rightmark >= leftmark:
            # print(f'{arr[rightmark]}, {pivot_val}, rm{rightmark}, lm{leftmark}')
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            arr[leftmark], arr[rightmark] = arr[rightmark], arr[leftmark]

    arr[first], arr[rightmark] = arr[rightmark], arr[first]

    return rightmark
