from copy import deepcopy


def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    sub = []
    for size in range(len(nums) + 1):
        _backtrack(size, 0, sub, res, nums)
    return res


def _backtrack(subset_size, start_index, temp_subset, result, nums):
    if len(temp_subset) == subset_size:
        result.append(deepcopy(temp_subset))
        return
    for i in range(start_index, len(nums)):
        temp_subset.append(nums[i])
        _backtrack(subset_size, i + 1, temp_subset, result, nums)
        temp_subset.pop(-1)


if __name__ == '__main__':
    print(subsets([1, 2, 3]))