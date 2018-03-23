def largest_product(arr):
    try:
        largest_sum = 0
        for i in range(len(arr)):
            product = arr[i][0] * arr[i][1]
            if product > largest_sum:
                largest_sum = product
        return largest_sum
    except (TypeError):
        print('No list is passed through')
