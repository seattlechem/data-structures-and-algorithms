from .fizz_buzz_tree import FizzBuzzTree


def test_FizzBuzzTree_true(five_element_bst):
    """ test for five element bst """
    ls = []
    FizzBuzzTree(five_element_bst)
    five_element_bst.in_order(lambda n: ls.append(n.val))
    assert ls == [0, 1, 'Fizz', 'Buzz', 'Fizz']


def test_FizzBuzzTree_eleven_true(eleven_element_bst):
    """ test for eleven element bst """
    ls = []
    FizzBuzzTree(eleven_element_bst)
    eleven_element_bst.pre_order(lambda n: ls.append(n.val))
    assert ls == [7, 1, 0, 'Fizz', 2, 'Buzz', 4, 'Fizz', 'Fizz', 8, 'Buzz']


def test_FizzBuzzTree_eleven_post_true(eleven_element_bst):
    """ test for eleven element bst """
    ls = []
    FizzBuzzTree(eleven_element_bst)
    eleven_element_bst.post_order(lambda n: ls.append(n.val))
    assert ls == [0, 2, 4, 'Fizz', 'Buzz', 'Fizz', 1, 8, 'Buzz', 'Fizz', 7]


def test_FizzBuzzTree_fizzbuzz(seven_element_bst):
    """ test for seven element bst """
    ls = []
    seven_element_bst.in_order(lambda n: ls.append(n.val))
    15, 10, 12, 23, 9, 0, 30
    assert ls == [0, 9, 10, 12, 15, 23, 30]
    ls = []
    FizzBuzzTree(seven_element_bst)
    seven_element_bst.in_order(lambda n: ls.append(n.val))
    assert ls == [0, 'Fizz', 'Buzz', 'Fizz', 'FizzBuzz', 23, 'FizzBuzz']
