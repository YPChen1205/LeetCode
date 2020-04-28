from copy import deepcopy


def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    com = []
    res = []
    _backtrack(com, res, 1, k, n)
    return res


def _backtrack(com, res, start, k, n):
    if k == 0:
        comb = deepcopy(com)  # important
        res.append(comb)
        return
    for i in range(start, n - k + 2):  # n- k + 1 consider the last k elements
        com.append(i)
        _backtrack(com, res, i + 1, k - 1, n)
        com.pop(-1)


if __name__ == '__main__':
    print(combine(4, 2))
