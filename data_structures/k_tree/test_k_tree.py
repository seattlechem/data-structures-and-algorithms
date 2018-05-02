"""Ptest cases."""
import pytest
from .k_tree import Node
from .k_tree import KTree as KT


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


def test_breadth_first_traversal(small_tree):
    """Confirm breadth_first_traversal."""
    ls = []
    small_tree.breadth_first_traversal(lambda n: ls.append(n.val))
    assert ls == [5, 9, 3]


def test_ktree_node():
    """Test if K-tree node is made properly."""
    nd = Node(34)
    assert nd.val == 34
    assert nd.children == []
    assert repr(nd) == '<Node Val: 34>'
    assert str(nd) == 'Node Val: 34'


def test_ktree(small_tree):
    """Test K-tree str and repr."""
    assert repr(small_tree) == '<KTree Root Val: 5>'
    assert str(small_tree) == 'KTree Root Val: 5'
