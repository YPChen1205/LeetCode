class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def binary_tree_paths(root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    res = []
    if root is None:
        return res
    vals = []
    backtrack(root, vals, res)
    return res


def backtrack(node, vals, res):
    if node is None:
        return
    vals.append(node.val)
    if node.left or node.right:
        backtrack(node.left, vals, res)
        backtrack(node.right, vals, res)
    else:
        res.append(build_path(vals))
    vals.pop(-1)


def build_path(vals):
    s = ''
    for i in range(len(vals)):
        s += str(vals[i])
        if i != len(vals) - 1:
            s += '->'
    return s


if __name__ == '__main__':
    nodes = []
    for i in range(1, 6):
        nodes.append(TreeNode(i))

    root = nodes[0]
    root.left = nodes[1]
    root.right = nodes[2]
    nodes[1].right = nodes[4]

    print(binary_tree_paths(root))