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

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val)
        if self.right:
            self.right.print_tree()

# class Tree(TreeNode):
#
#     def __init__(self, root):
#         self.root = root
#
#     def create_tree(self, nodes):
#
#         for node in nodes:
#             if not self.root.left:
#                 self.root.left = node
#             elif not self.root.right:
#                 self.root.right = node
#             else:
#                 self.create_nodes()
