class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def __repr__(self):
        return '<Node Val: {}>'.format(self.val)

    def __str__(self):
        return self.val


class BST:
    def __init__(self, iter=[]):
        self.root = None
        if not isinstance(iter, (str, tuple, list)):
            raise TypeError('It\'s not an iterable type.')
        for item in iter:
            self.insert(item)

    def __repr__(self):
        return '<BST Root: {}>'.format(self.root.val)

    def __str__(self):
        val = self.root.val
        return str(val)

    def in_order(self, operation):
        def _walk(node=None):
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)

            operation(node)

            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def pre_order(self, operation):
        def _walk(node=None):
            if node is None:
                return

            operation(node)

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def post_order(self, operation):
        def _walk(node=None):
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)

            operation(node)

        _walk(self.root)

    def insert(self, val):
        if isinstance(val, Node):
            node = val
        else:
            node = Node(val)

        current = self.root

        if self.root is None:
            self.root = node
            return node

        while current:
            try:
                if val >= current.val:
                    if current.right is not None:
                        current = current.right
                    else:
                        current.right = node
                        break

                elif val < current.val:
                    if current.left is not None:
                        current = current.left
                    else:
                        current.left = node
                        break
            except TypeError:
                raise TypeError('the value cannot be compared')

        return node
