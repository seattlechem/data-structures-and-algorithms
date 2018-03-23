from binary_search import binary_search


def test_binary_search_true():
    assert binary_search([4, 8, 15, 16, 23, 42], 15) == 2


def test_binary_search_false():
    assert binary_search([11, 22, 33, 44, 55, 66, 77], 90) == -1


def test_binary_search_empty_list():
    assert binary_search([], 90) == -1


def test_binary_search_string():
    assert binary_search(['potato', 'tomato', 'new york'], 'tomato') == 1
