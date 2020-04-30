from copy import deepcopy


def combination_sum_3(k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    res = []
    _backtrack(res, [], k, n, 0, range(1, 10))
    return res


def _backtrack(res, comb, k, target, start, candidates):
    if not k and not target:
        res.append(deepcopy(comb))
        return
    if not k or not target:
        return
    for i in range(start, 9):
        if i <= target:
            comb.append(candidates[i])
            _backtrack(res, comb, k-1, target-candidates[i], i+1, candidates)
            comb.pop(-1)


if __name__ == '__main__':
    print(combination_sum_3(3, 7))
    print(combination_sum_3(3, 9))
