def inorder_traversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res = []
    if root is None:
        return res
    stack = []
    cur = root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        node = stack[-1]
        stack.pop()
        res.append(node.val)
        cur = node.right
    return res

