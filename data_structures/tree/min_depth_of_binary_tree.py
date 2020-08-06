def min_depth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    left = min_depth(root.left)
    right = min_depth(root.right)
    if left==0 or right==0:
        return left+right+1
    return min(left, right)+1

