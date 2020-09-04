from collections import Counter


def find_mode(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    nums = []
    cnt = Counter()
    __in_order(root, nums)
    nums2 = [nums[i] for i in range(len(nums)) if nums[i]] # reduce None in nums
    for num in nums2:
        cnt[num] += 1
    cnt = dict(cnt)
    max_cnt = max(cnt.values())
    ret = [k for k,v in cnt.items() if v == max_cnt]
    return ret


def __in_order(root, num):
    if not root:
        return
    __in_order(root.left,num)
    num.append(root.val)
    __in_order(root.right, num)


if __name__ == '__main__':
    import tree2 as t
    root = t.TreeNode.create_binary_tree([1,None,2,None,None,2])
    print(find_mode(root))