from .fizz_buzz_tree import FizzBuzzTree


def test_FizzBuzzTree_True(five_element_bst):
    ls = []
    FizzBuzzTree(five_element_bst)
    five_element_bst.in_order(lambda n: ls.append(n.val))
    assert ls == [0, 1, 'Fizz', 'Buzz', 'Fizz']


def test_FizzBuzzTree_eleven_True(eleven_element_bst):
    ls = []
    FizzBuzzTree(eleven_element_bst)
    eleven_element_bst.pre_order(lambda n: ls.append(n.val))
    assert ls == [7, 1, 0, 'Fizz', 2, 'Buzz', 4, 'Fizz', 'Fizz', 8, 'Buzz']
