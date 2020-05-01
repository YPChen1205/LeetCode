def trim_bst(root, l, r):
    """
    :type root: TreeNode
    :type l: int
    :type r: int
    :rtype: TreeNode
    """
    if not root:
        return None
    if root.val > r:
        return trim_bst(root.left, l, r)
    if root.val < l:
        return trim_bst(root.right, l, r)
    root.left = trim_bst(root.left, l, r)
    root.right = trim_bst(root.right, l, r)
    return root
