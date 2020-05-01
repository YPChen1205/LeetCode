from copy import deepcopy


def subsets_with_dup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    res = []
    for size in range(len(nums) + 1):
        _backtrack(0, size, [], res, nums)
    return res


def _backtrack(start_index, subset_size, temp_subset, result, nums):
    if len(temp_subset) == subset_size:
        result.append(deepcopy(temp_subset))
        return
    for i in range(start_index, len(nums)):
        if i > start_index and nums[i] == nums[i - 1]:  # critical
            continue
        temp_subset.append(nums[i])
        _backtrack(i + 1, subset_size, temp_subset, result, nums)
        temp_subset.pop(-1)


if __name__ == '__main__':
    print(subsets_with_dup([1, 2, 2]))
