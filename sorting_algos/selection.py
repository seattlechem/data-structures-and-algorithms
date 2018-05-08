"""Selection Sort."""


def selection(ls):
    """Create a function which sort list by selection."""

    if type(ls) is not list:
        raise TypeError('Input must be a list type.')

    for i in range(0, len(ls)):
        if not isinstance(ls[i], int):
            raise TypeError('All elements must be an integer.')

    if len(ls) <= 1:
        return ls

    index_of_min = 0

    for i in range(0, len(ls)):
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[index_of_min]:
                index_of_min = j
                ls[i], ls[j] = ls[j], ls[i]
            index_of_min = i

    return ls
