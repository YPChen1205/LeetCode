class Solution(object):
    def __init__(self):
        self.ans = True

    def is_balanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.max_depth(root)
        return self.ans

    def max_depth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            l = self.max_depth(root.left)
            r = self.max_depth(root.right)
            if abs(l - r) > 1:
                self.ans = False
            return max(l, r) + 1
        else:
            return 0


if __name__ == '__main__':
    import tree as t

    nodes1 = t.TreeNode.create_nodes([3, 9, 20, 15, 7])

    root1 = nodes1[0]
    root1.left = nodes1[1]
    root1.right = nodes1[2]
    nodes1[2].left = nodes1[3]
    nodes1[2].right = nodes1[4]

    sol1 = Solution()
    print(Solution.is_balanced(sol1, root1))

    nodes2 = t.TreeNode.create_nodes([1, 2, 2, 3, 3, 4, 4])

    root2 = nodes2[0]
    root2.left = nodes2[1]
    root2.right = nodes2[2]
    nodes2[1].left = nodes2[3]
    nodes2[1].right = nodes2[4]
    nodes2[3].left = nodes2[5]
    nodes2[3].right = nodes2[6]

    sol2 = Solution()
    print(Solution.is_balanced(sol2, root2))
