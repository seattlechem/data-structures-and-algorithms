"""Create test KTree."""
from .k_tree import KTree
from .k_tree import Node
import pytest


@pytest.fixture
def small_tree():
    """Make an instance of small KTree object."""
    tree = KTree()
    tree.root = Node(5)
    tree.root.children = [Node(9), Node(3)]
    return tree


@pytest.fixture
def large_tree():
    """Make an instance of large KTree object."""
    tree = KTree()
    tree.root = Node(12)
    tree.root.children = [Node(9), Node(2), Node(11)]
    tree.root.children[0].children = [Node(1), Node(3)]
    tree.root.children[1].children = [Node(99)]
    tree.root.children[1].children[0].children = [Node(13), Node(14)]
    return tree
