def path_sum_i(root, sum):
    if not root:
        return False
    if root.val == sum and not root.left and not root.right:
        return True
    return path_sum_i(root.left, sum - root.val) or path_sum_i(root.right, sum - root.val)


if __name__ == '__main__':
    import tree as t

    nodes = t.TreeNode.create_nodes([5, 4, 8,11,13,4,7, 2, 1])
    root = nodes[0]
    root.left = nodes[1]
    root.right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[2].left = nodes[4]
    nodes[2].right = nodes[5]
    nodes[3].left = nodes[6]
    nodes[3].right = nodes[7]
    nodes[5].right = nodes[8]
    t.TreeNode.print_tree(root)

    print(path_sum_i(root, 22))
