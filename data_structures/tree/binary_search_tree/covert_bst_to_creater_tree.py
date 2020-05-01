def convert_bst(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """

    new_value = 0

    node = root
    stack = []
    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.right

        node = stack.pop()
        new_value += node.val
        node.val = new_value

        node = node.left

    return root
