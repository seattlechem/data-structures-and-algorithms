def insertShiftArray(arr, num):
    if type(arr) is not list or type(num) is not int:
        raise TypeError('Argument(s) invalid.')
    lis = list(range(len(arr) + 1))
    for i in range(len(arr)):
        lis[i] = arr[i]
    length = len(arr)
    if length % 2:
        length += 1
    mid = length // 2
    counter = 1
    while counter <= mid:
        temp = lis[-counter]
        lis[-counter] = lis[-(counter + 1)]
        lis[-(counter + 1)] = temp
        counter += 1
    lis[mid] = num
    return lis
