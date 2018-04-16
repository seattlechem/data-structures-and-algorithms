def fizz_buzz_op(nd):
    """ fizz_buzz function which takes node """

    if nd.val != 0:
        if nd.val % 15 == 0:
            nd.val = 'FizzBuzz'

        elif nd.val % 3 == 0:
            nd.val = 'Fizz'

        elif nd.val % 5 == 0:
            nd.val = 'Buzz'


def FizzBuzzTree(binary_tree):
    """ fizz buzz tree function which takes bst """
    binary_tree.in_order(fizz_buzz_op)
