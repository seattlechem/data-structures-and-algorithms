from .bst import BST


def find_maximum_value(bst):
    """ function finding max value from bst input \
        it checks if input is of BST type \
        and if root is empty
    """
    if not isinstance(bst, BST):
        raise TypeError('It\'s not a BST type.')

    if bst.root is None:
        raise ValueError('BST is empty.')

    max = 0
    this_level = [bst.root]

    while this_level:
        next_level = list()
        for n in this_level:
            if n.val > max:
                max = n.val
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
        this_level = next_level

    return max
