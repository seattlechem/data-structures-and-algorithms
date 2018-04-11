from .bst import BST


def breadthFirstTraversal(bst):
    if not isinstance(bst, BST):
        raise TypeError('It\'s not a BST type.')

    ls = []
    thislevel = [bst.root]

    while thislevel:
        nextlevel = list()
        for n in thislevel:
            ls.append(n.val)
            if n.left:
                nextlevel.append(n.left)
            if n.right:
                nextlevel.append(n.right)
        thislevel = nextlevel
    return ls
