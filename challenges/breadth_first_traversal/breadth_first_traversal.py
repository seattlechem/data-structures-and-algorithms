def breadthFirstTraversal(bst):
    thislevel = [bst.root]
    while thislevel:
        nextlevel = list()
        for n in thislevel:
            print(n.value)
            if n.left:
                nextlevel.append(n.left)
            if n.right:
                nextlevel.append(n.right)
        thislevel = nextlevel
