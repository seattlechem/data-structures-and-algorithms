import pytest


def test_inorder_true(eleven_element_bst):
    ls = []
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    eleven_element_bst.in_order(lambda n: ls.append(n.val))
    assert ls == expected


def test_preorder_true(eleven_element_bst):
    ls = []
    expected = [7, 1, 0, 3, 2, 5, 4, 6, 9, 8, 10]
    eleven_element_bst.pre_order(lambda n: ls.append(n.val))
    assert ls == expected


def test_postorder_true(eleven_element_bst):
    ls = []
    expected = [0, 2, 4, 6, 5, 3, 1, 8, 10, 9, 7]
    eleven_element_bst.post_order(lambda n: ls.append(n.val))
    assert ls == expected


def test_insert_type_error(eleven_element_bst):
    with pytest.raises(TypeError):
        eleven_element_bst.insert('b')


def test_root_val_true(eleven_element_bst):
    assert eleven_element_bst.root.val == 7
