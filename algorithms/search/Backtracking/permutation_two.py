from copy import copy, deepcopy


def permute_unique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    permute = []
    nums.sort()
    visited = [False for n in nums]
    _backtrack(permute, res, visited, nums)
    return res


def _backtrack(permute, res, visited, nums):
    if len(permute) == len(nums):
        perm = deepcopy(permute)  # critical
        res.append(perm)
        return
    for i in range(len(nums)):
        if i != 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
            continue
        if visited[i]:
            continue
        visited[i] = True
        permute.append(nums[i])
        _backtrack(permute, res, visited, nums)
        permute.pop(-1)
        visited[i] = False


if __name__ == '__main__':
    print(permute_unique([1, 1, 2]))
