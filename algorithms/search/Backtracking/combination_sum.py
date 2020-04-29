from copy import deepcopy


def combination_sum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    _backtrack([], res, 0, target, candidates)
    return res


def _backtrack(comb, res, start, target, candidates):
    if not target:
        res.append(deepcopy(comb))
        return
    for i in range(start, len(candidates)):
        if candidates[i] <= target:
            comb.append(candidates[i])
            _backtrack(comb, res, i, target - candidates[i], candidates)
            comb.pop(-1)


if __name__ == '__main__':
    print(combination_sum([2, 3, 6, 7], 7))
