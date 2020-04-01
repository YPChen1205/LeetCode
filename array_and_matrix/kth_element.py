import numpy as np


def kth_smallest(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    matrix = np.array(matrix)
    n, _ = matrix.shape

    l = matrix[0, 0]
    u = matrix[n - 1, n - 1]
    while l <= u:
        cnt = 0
        mid = (l + u) // 2
        for i in range(n):
            for j in range(n):
                if matrix[i, j] <= mid:
                    cnt += 1
        if cnt < k:
            l = mid+1
        else:
            u = mid-1
    return l


if __name__ == '__main__':
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8
    print(kth_smallest(matrix, k))
