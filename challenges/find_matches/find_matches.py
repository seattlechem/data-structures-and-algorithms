"""Function to find all matching nodes in a linked list."""

from .linked_list import LinkedList
from .node import Node
from .k_tree import KTree


def find_matches(ktree, target_value):
    """
    Perform search for all nodes.

    if node's value matches with target_value, the node is
    added to the linked list.

    """
    ls = list()

    def _walk(curr=None):
        """Define a helper function which traverses ktree."""
        if curr is None:
            return

        if curr.val == target_value:
            ls.append(curr)

        for child in curr.children:
            _walk(child)

    _walk(ktree.root)

    return ls
