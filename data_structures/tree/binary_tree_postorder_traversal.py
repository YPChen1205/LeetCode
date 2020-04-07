def postorder_traversal(root):
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
        stack.append(node.left)
        stack.append(node.right)
    res.reverse()
    return res
