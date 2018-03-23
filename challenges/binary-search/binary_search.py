def binary_search(arr, search_key):
    for i in range(len(arr)):
        if arr[i] == search_key:
            return i
    return -1
