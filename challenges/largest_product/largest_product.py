def largest_product(arr):
    largest_sum = 0
    try:
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if j != len(arr[0]) - 1:
                    product = arr[i][j] * arr[i][j + 1]
                if i != len(arr) - 1:
                    product2 = arr[i][j] * arr[i + 1][j]
                if product > product2:
                    largest_sum = product
                elif product2 > product:
                    largest_sum = product2
                elif product == product2:
                    largest_sum = product
    except TypeError:
        raise TypeError('Numbers only!')
    return largest_sum
