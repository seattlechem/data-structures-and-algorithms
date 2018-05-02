"""Tree Intercept."""
from .bst import BST


def tree_intercept(bst_1, bst_2):
    """Search 2 bsts and find intercept."""
    if type(bst_1) and type(bst_2) is not BST:
        raise TypeError('Input must be BST.')

    set1 = set()
    set2 = set()
    result = []

    bst_1.pre_order(lambda n: set1.add(n.val))
    bst_2.pre_order(lambda n: set2.add(n.val))

    for value in set2:
        if value in set1:
            result.append(value)

    return result
