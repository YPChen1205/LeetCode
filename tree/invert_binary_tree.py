def invert_tree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root:
        l = invert_tree(root.left)
        r = invert_tree(root.right)
        root.left = r
        root.right = l
        return root
    else:
        return None


if __name__ == '__main__':
    import tree as t

    nodes = t.TreeNode.create_nodes([4, 2, 7, 1, 3, 6, 9])

    root = nodes[0]
    root.left = nodes[1]
    root.right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[5]
    nodes[2].right = nodes[6]

    t.TreeNode.print_tree(root)
    t.TreeNode.print_tree(invert_tree(root))




