"""Ptest cases."""
import pytest


def test_insert_small_ktree(small_tree):
    """This checks if a value inserted correctly."""
    # import pdb; pdb.set_trace()
    small_tree.insert(11, 3)
    assert small_tree.root.children[1].children[0].val == 11


def test_insert_small_ktree_no_parent(small_tree):
    """This tests if ValueError is raised when passing no parent."""
    with pytest.raises(ValueError):
        small_tree.insert(8)


def test_pre_order_traverse(small_tree):
    """Confirm pre_order traversal."""
    ls = []
    small_tree.pre_order(lambda n: ls.append(n.val))
    assert ls == [5, 9, 3]


def test_post_order_traversal(small_tree):
    """Confirm post_order traversal."""
    ls = []
    small_tree.post_order(lambda n: ls.append(n.val))
    assert ls == [9, 3, 5]
