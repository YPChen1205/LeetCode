import tree2 as t


def get_minimum_difference(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    nums = []
    __in_order(root, nums)
    diff = [nums[i] - nums[i-1] for i in range(1,len(nums)) if nums[i] and nums[i-1]]
    return min(diff)


def __in_order(root, num):
    if not root:
        return
    __in_order(root.left,num)
    num.append(root.val)
    __in_order(root.right, num)


if __name__ == '__main__':
    import tree2 as t
    root = t.TreeNode.create_binary_tree([1,None,3,None,None,2])
    print(get_minimum_difference(root))