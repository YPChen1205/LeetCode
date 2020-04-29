from copy import deepcopy


def combination_sum_2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    visited = [False for cand in candidates]
    candidates.sort()
    _backtrack([], res, visited, 0, target, candidates)
    return res


def _backtrack(comb, res, visited, start, target, candidates):
    if not target:
        res.append(deepcopy(comb))
        return
    for i in range(start, len(candidates)):
        if i == 0 and candidates[i] == candidates[i - 1] and not visited[i - 1]:
            continue
        if candidates[i] <= target:
            comb.append(candidates[i])
            visited[i] = True
            _backtrack(comb, res, visited, i + 1, target - candidates[i], candidates)
            visited[i] = False
            comb.pop(-1)


if __name__ == '__main__':
    print(combination_sum_2([10, 1, 2, 7, 6, 1, 5], 8))
