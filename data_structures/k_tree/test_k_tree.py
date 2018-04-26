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
