def insertShiftArray(arr, num):
    mid = len(arr)/2
    temp = arr[mid]
    arr[mid] = num
    for mid in range(len(arr)):
        temp2 = arr[mid + 1]
        arr[mid + 1] = temp



arr = [2,4,6,8]
num = 5
