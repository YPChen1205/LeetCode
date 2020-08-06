def same_tree(s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """
    if not s and not t:
        return True
    if not s or not t:
        return False
    if t.val != s.val:
        return False
    return same_tree(s.left, t.left) and same_tree(s.right, t.right)


def is_subtree(s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """
    if not s:
        return False

    return same_tree(s,t) or same_tree(s.right, t) or same_tree(s.left, t)