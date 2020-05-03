from tree import TreeNode


def sorted_array_to_bst(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    return _to_bst(nums, 0, len(nums) - 1)


def _to_bst(nums, start_idx, end_idx):
    if start_idx > end_idx:
        return None
    mid_idx = int(start_idx + (end_idx - start_idx) // 2)
    root = TreeNode(nums[mid_idx])
    root.left = _to_bst(nums, start_idx, mid_idx - 1)
    root.right = _to_bst(nums, mid_idx + 1, end_idx)
    return root

