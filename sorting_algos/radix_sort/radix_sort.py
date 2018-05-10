"""Radix Sort."""


def radix_sort(arr):
    """Return list sorted by radix sort."""
    len_arr = len(arr)
    modulus = 10
    div = 1
    while True:
        # empty array, [[] for i in range(10)]
        new_list = [[], [], [], [], [], [], [], [], [], []]
        for value in arr:
            least_digit = value % modulus
            least_digit /= div
            new_list[least_digit].append(value)
        modulus = modulus * 10
        div = div * 10

        if len(new_list[0]) == len_arr:
            return new_list[0]

        arr = []
        rd_list_append = arr.append
        for x in new_list:
            for y in x:
                rd_list_append(y)

    
