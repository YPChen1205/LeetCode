class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def generate_trees(n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    if n <= 1:
        return TreeNode(n)
    return generate_subtrees(1, n)


def generate_subtrees(s, e):
    """
    :param s: start
    :param e: end
    :return: List[TreeNode]
    """
    res = []
    if s > e:
        res.append(None)
        return res
    for i in range(s, e + 1):
        left_subtrees = generate_subtrees(s, i - 1)
        right_subtrees = generate_subtrees(i + 1, e)
        for l in left_subtrees:
            for r in right_subtrees:
                root = TreeNode(i)
                root.left = l
                root.right = r
    return res


if __name__ == '__main__':
    print(generate_trees(3))
