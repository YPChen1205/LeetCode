def path_sum_start_with(node, sum):
    if not node: return 0
    ret = 0
    if node.val == sum: ret += 1
    ret += path_sum_start_with(node.left, sum-node.val) + path_sum_start_with(node.right, sum-node.val)
    return ret


def path_sum_iii(root, sum):
    if not root:
        return 0
    ret = path_sum_start_with(root, sum) + path_sum_start_with(root.left, sum) + path_sum_start_with(root.right, sum)
    return ret


if __name__ == '__main__':
    import tree as t
    nodes = t.TreeNode.create_nodes([10,5, -3, 3, 2,11, 3,-2, 1])
    root = nodes[0]
    root.left = nodes[1]
    root.right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].right = nodes[5]
    nodes[3].left = nodes[6]
    nodes[3].right = nodes[7]
    nodes[4].right = nodes[8]
    # t.TreeNode.print_tree(root)

    print(path_sum_iii(root, 8))

