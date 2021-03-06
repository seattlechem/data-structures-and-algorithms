from .breadth_first_traversal import breadthFirstTraversal
import pytest


def test_simple_bst(five_element_bst):
    result = breadthFirstTraversal(five_element_bst)
    assert result == [5, 1, 9, 0, 3]


def test_non_bst():
    with pytest.raises(TypeError):
        breadthFirstTraversal([1, 2, 3, 4, 5])


def test_seven_bst(seven_element_bst):
    result = breadthFirstTraversal(seven_element_bst)
    assert result == [15, 10, 23, 9, 12, 30, 0]
