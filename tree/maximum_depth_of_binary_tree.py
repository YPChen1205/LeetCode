def max_depth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root:
        return max(max_depth(root.left), max_depth(root.right)) + 1
    else:
        return 0


if __name__ == '__main__':
    import tree as t

    nodes = t.TreeNode.create_nodes([3, 9, 20, 15, 7])
    root = nodes[0]
    root.left = nodes[1]
    root.right = nodes[2]
    nodes[2].left = nodes[3]
    nodes[2].right = nodes[4]

    print(max_depth(root))
