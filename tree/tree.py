# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


    def create_nodes(values):
        nodes = []
        for val in values:
            if val:
                nodes.append(TreeNode(val))
        return nodes

