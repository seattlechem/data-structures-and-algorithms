def fizz_buzz_op(nd):

    if nd.val != 0:
        if nd.val % 15 == 0:
            nd.val = 'FizzBuzz'

        elif nd.val % 3 == 0:
            nd.val = 'Fizz'

        elif nd.val % 5 == 0:
            nd.val = 'Buzz'


def FizzBuzzTree(binary_tree):
    binary_tree.in_order(fizz_buzz_op)
