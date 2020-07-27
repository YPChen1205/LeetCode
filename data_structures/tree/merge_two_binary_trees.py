def merge_trees(t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    t1.val += t2.val
    t1.left = merge_trees(t1.left, t2.left)
    t1.right = merge_trees(t1.right, t2.right)
    return t1


if __name__ == '__main__':
    import tree as t
    nodes1 = t.TreeNode.create_nodes([1,3,2,5])
    t1 = nodes1[0]
    t1.left = nodes1[1]
    t1.right = nodes1[2]
    nodes1[1].left = nodes1[3]

    t.TreeNode.print_tree(t1)

    print("---")
    nodes2 = t.TreeNode.create_nodes([2,1,3,4,7])
    t2 = nodes2[0]
    t2.left = nodes2[1]
    t2.right = nodes2[2]
    nodes2[1].right = nodes2[3]
    nodes2[2].right = nodes2[4]

    t.TreeNode.print_tree(t2)
    print("---")
    t.TreeNode.print_tree(merge_trees(t1,t2))