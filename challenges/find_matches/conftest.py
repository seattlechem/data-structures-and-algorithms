"""This page contains several functions that create various KAry Trees."""
import pytest
from .k_tree import KTree
from .node import Node


@pytest.fixture
def small_tree():
    """Create a small ktree."""
    tree = KTree()
    tree.root = Node(3)

    tree.children = [Node(5), Node(6), Node(7), Node(5)]
    tree.children[0].children = [Node(5), Node(11)]
