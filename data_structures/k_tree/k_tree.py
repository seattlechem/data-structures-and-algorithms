class Node:
    def __init__(self, val=None):
        """ create an instance of Node object """
        self.val = val
        self.children = []

    def __repr__(self):
        """ node class representation """
        return '<Node Val: {}>'.format(self.val)

    def __str__(self):
        """ node class string printout """
        return self.val


class KTree:
    def __init__(self):
        """ create an instance of KTree object """
        self.root = None

    def __repr__(self):
        """ KTree class representation """
        return '<KTree Root Val: {}>'.format(self.root.val)

    def __str__(self):
        """ KTree class string printout """
        return self.root.val

    def pre_order(self, operation):
        """ KTree pre_order traversal """
        def _walk(node=None):
            if node is None:
                return

            operation(node)

            if node.children is not None:
                for child in node.children:
                    _walk(child)

        _walk(self.root)

    def post_order(self, operation):
        """ KTree post_order traversal """
        def _walk(node=None):
            if node is None:
                return

            if node.children is not None:
                for child in node.children:
                    _walk(child)

                operation(node)

        _walk(self.root)
        
