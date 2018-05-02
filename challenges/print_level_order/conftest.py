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
