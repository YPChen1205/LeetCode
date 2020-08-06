def is_same_tree(s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """
    if not s and not t:
        return True
    elif s and t:
        if s.val != t.val:
            return False
        else:
            return is_same_tree(s.left, t.left) and is_same_tree(s.right, t.right)
    else:
        return False


def is_symmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    if not root.left and not root.right:
        return True
    elif root.left and root.right:
        return is_same_tree(root.left, root.right)
    else:
        return False

