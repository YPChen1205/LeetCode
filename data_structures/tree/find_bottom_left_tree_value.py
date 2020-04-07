def find_bottom_left_value(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    queue = [root]  # use queque to ensure lay by lay traverse
    while queue:
        root = queue[0]
        queue.pop(0)
        if root.right:  # first add the right to ensure the last element is left most
            queue.append(root.right)
        if root.left:
            queue.append(root.left)
    return root.val


if __name__ == '__main__':
    import tree as t

    nodes = t.TreeNode.create_nodes([1, 2, 3, 4, 5, 6, 7])
    root = nodes[0]
    root.left = nodes[1]
    root.right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[2].left = nodes[4]
    nodes[2].right = nodes[5]
    nodes[4].left = nodes[6]

    print(find_bottom_left_value(root))
