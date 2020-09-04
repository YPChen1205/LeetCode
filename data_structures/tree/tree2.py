# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def create_binary_tree(values):
        """
        :type: list
        :return:  created tree
        """
        # change values into tree nodes
        nodes = []
        for val in values:
            nodes.append(TreeNode(val))
        # print(nodes)

        n = len(values)  # number of nodes
        # print(n)

        if n % 2 == 1:  # last node is a right child with the idx n-1
            m_idx = max(int((n - 3)/ 2), 0)  # (n-1 -2)/2
        else:  # last node is a left child
            m_idx = max(int(n / 2) - 1, 0)  # (n-1 - 1)/2

        for i in range(m_idx):
            nodes[i].left = nodes[2 * i + 1]
            nodes[i].right = nodes[2 * i + 2]
        if 2*m_idx + 2 <= n:
            nodes[m_idx].left = nodes[2*m_idx+1]
        if 2*m_idx + 3 <= n:
            nodes[m_idx].right = nodes[2*m_idx+2]

        root = nodes[0]
        return root

    def inorder_print_tree(self):
        if self.left:
            self.left.inorder_print_tree()
        print(self.val)
        if self.right:
            self.right.inorder_print_tree()


if __name__ == '__main__':
    root = TreeNode.create_binary_tree([5, 3, 6, 2, 4, None, 7])
    root.inorder_print_tree()
#     l1_2 = root.right

