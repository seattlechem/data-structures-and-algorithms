def insertShiftArray(arr, num):
    mid = len(arr) // 2
    lis = list(range(len(arr) + 1))
    for i in range(len(arr)):
        lis[i] = arr[i]
    counter = 1
    while counter <= mid:
        temp = lis[len(lis) - counter]
        lis[len(lis) - counter] = lis[len(lis) - (counter + 1)]
        lis[len(lis) - (counter + 1)] = temp
        counter += 1
    lis[mid] = num
    return lis
