def find_target(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: bool
    """
    nums = []
    __inorder(root, nums)
    i = 0
    j = len(nums)-1
    while i < j:
        num_sum = nums[i] + nums[j]
        if num_sum == k:
            return True
        if num_sum < k:
            i += 1
        else:
            j -= 1
    return False

def __inorder(root, nums):
    if not root:
        return
    __inorder(root.left, nums)
    nums.append(root.val)
    __inorder(root.right, nums)


if __name__ == '__main__':
    import tree2 as t
    root = t.TreeNode.create_binary_tree([5,3,6,2,4,None,7])


