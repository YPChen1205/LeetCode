class Solution(object):
    def diameter_of_binary_tree(self, root):
        self.ans = 1
        def depth(node):
            if not node: return 0
            l = depth(node.left)
            r = depth(node.right)
            self.ans = max(self.ans, l+r+1)
            return max(l, r) + 1
        depth(root)

        return self.ans - 1



if __name__ == '__main__':
   import tree as t
   nodes = t.TreeNode.create_nodes([1,2,3,4,5])
   root = nodes[0]
   root.left = nodes[1]
   root.right = nodes[2]
   nodes[1].left = nodes[3]
   nodes[1].right = nodes[4]
   sol = Solution()
   print(Solution.diameter_of_binary_tree(sol, root))

