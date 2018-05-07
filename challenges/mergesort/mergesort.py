
def merge(left, right):
    """Two lists are merged."""
    results = []

    while len(left) and len(right):
        if left[0] < right[0]:
            results.append(left.shift())
        else:
            results.append(right.shift())
    return [results[::], left[::], right[::]]
