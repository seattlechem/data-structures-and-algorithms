"""Selection Sort."""


def selection(ls):
    """Create a function which sort list by selection."""
    index_of_min = 0

    for i in range(0, len(ls)):
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[index_of_min]:
                index_of_min = j
                ls[i], ls[j] = ls[j], ls[i]
            index_of_min = i

    return ls
