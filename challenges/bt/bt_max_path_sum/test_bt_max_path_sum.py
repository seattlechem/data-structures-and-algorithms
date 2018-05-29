"""Test cases."""
from .bt_max_path_sum import tree_node
from .bt_max_path_sum import max_path_sum


test_bt = tree_node(5)
test_bt.left = tree_node(-10)
test_bt.right = tree_node(7)
test_bt.left.left = tree_node(3)
test_bt.left.right = tree_node(8)
test_bt.right.left = tree_node(9)
test_bt.right.right = tree_node(-1)


def test_max_path_sum():
    """Assert if answer is correct."""
    result = max_path_sum(test_bt)
    assert result == 21
