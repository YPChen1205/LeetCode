from tree import TreeNode

def average_of_levels(root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    res = []
    if root is None:
        return []
    queue = [root]
    while queue:
        sum_layer = 0
        count = 0
        temp = []
        while queue:
            n = queue[0]
            queue.pop(0)
            sum_layer += n.val
            count += 1
            if n.left:
                temp.append(n.left)
            if n.right:
                temp.append(n.right)
        queue = temp
        res.append(sum_layer * 1.0 / count)
    return res


if __name__ == '__main__':
    nodes = TreeNode.create_nodes([3, 9, 20, 15, 7])
    root = nodes[0]
    root.left = nodes[1]
    root.right = nodes[2]
    nodes[2].left = nodes[3]
    nodes[2].right = nodes[4]

    print(average_of_levels(root))
