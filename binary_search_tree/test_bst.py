import pytest


def test_inorder_true(eleven_element_bst):
    """ in_order traversal test """
    ls = []
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    eleven_element_bst.in_order(lambda n: ls.append(n.val))
    assert ls == expected


def test_inorder_empty(empty_bst):
    """ in_order traversal on empty bst instance """
    assert empty_bst.in_order(lambda n: print(n)) is None


def test_preorder_true(eleven_element_bst):
    """ pre_order traversal test """
    ls = []
    expected = [7, 1, 0, 3, 2, 5, 4, 6, 9, 8, 10]
    eleven_element_bst.pre_order(lambda n: ls.append(n.val))
    assert ls == expected


def test_preorder_empty(empty_bst):
    """ pre_order traversal on empty bst instance """
    assert empty_bst.pre_order(lambda n: print(n)) is None


def test_postorder_true(eleven_element_bst):
    """ post_order traversal test """
    ls = []
    expected = [0, 2, 4, 6, 5, 3, 1, 8, 10, 9, 7]
    eleven_element_bst.post_order(lambda n: ls.append(n.val))
    assert ls == expected


def test_postorder_empty(empty_bst):
    """ post_order on empty bst instance """
    assert empty_bst.post_order(lambda n: print(n)) is None


def test_insert_type_error(eleven_element_bst):
    """ insert method test """
    with pytest.raises(TypeError):
        eleven_element_bst.insert('b')


def test_root_val_true(eleven_element_bst):
    """ test for root value """
    assert eleven_element_bst.root.val == 7


def test_non_iteralbe_init(empty_bst):
    """ test for when constructing a bst with non iterable argument """
    with pytest.raises(TypeError):
        empty_bst(2)


def test_repr_bst(eleven_element_bst):
    """ test for bst representation """
    assert repr(eleven_element_bst) == '<BST Root: 7>'


def test_str_bst(eleven_element_bst):
    """ test for string print out """
    assert str(eleven_element_bst) == '7'
