def construct_array(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[int]
    """
    ori = [i for i in range(1, n + 1)]
    res = [i for i in range(1, n + 1)]
    j = -1
    p = n - k - 1
    for i in range(n - k - 1, n, 2):
        res[i] = ori[p]
        if i + 1 < n:
            res[i + 1] = ori[j]
            j -= 1
        p += 1

    return res


if __name__ == '__main__':
    print(construct_array(3, 1))
    print(construct_array(3, 2))
    print(construct_array(6, 3))
