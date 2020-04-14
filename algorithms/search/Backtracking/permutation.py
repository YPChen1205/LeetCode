from copy import deepcopy


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    perm = []
    visited = [False for n in nums]
    backtrack(nums, visited, perm, res)
    return res


def backtrack(nums, visited, perm, res):
    if len(perm) == len(nums):
        sol = deepcopy(perm)
        res.append(sol)
        return
    for i, n in enumerate(nums):
        if visited[i]:
            continue
        visited[i] = True
        perm.append(n)
        backtrack(nums, visited, perm, res)
        perm.pop(-1)
        visited[i] = False


if __name__ == '__main__':
    print(permute([1, 2, 3]))
