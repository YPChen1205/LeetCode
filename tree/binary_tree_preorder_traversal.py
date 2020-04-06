def preorder_traversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res = []
    stack = [root]
    while stack:
        node = stack[-1]
        stack.pop()
        if node is None:
            continue
        res.append(node.val)
        stack.append(node.right)
        stack.append(node.left)
    return res


if __name__ == '__main__':
    import tree as t
    nodes = t.TreeNode.create_nodes([1,2,3])
    root = nodes[0]
    root.right = nodes[1]
    nodes[1].left = nodes[2]

    print(preorder_traversal(root))
