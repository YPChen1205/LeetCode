import numpy as np


def search_matrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    matrix = np.array(matrix)
    if matrix.size != 0:
        n, m = matrix.shape
        if n == 0 or m == 0:
            return False
        diag = [matrix[i, i] for i in range(min(n, m))]
        u = binary_search_boundary(diag, target)
        if diag[u] == target:
            return True
        if u >= max(n, m):
            return False
        if u >= n and u < m:
            condidate = binary_search_boundary(matrix[u - 1, u - 1:], target)
            if matrix[n, condidate] == target:
                return True
        if u >= m and u < n:
            condidate = binary_search_boundary(matrix[u - 1:, u - 1], target)
            if matrix[condidate, n] == target:
                return True
        else:
            condidate = binary_search_boundary(matrix[u, :u], target)
            if matrix[u, condidate] == target:
                return True
            condidate = binary_search_boundary(matrix[:u, u], target)
            if matrix[condidate, u] == target:
                return True
    return False


def binary_search_boundary(nums, target):
    """
    search in a list of numbers where the target should located, if the target in nums
    return the exact position else return the high bundary position
    :param nums: List[int]
    :param target: int
    :return: int
    """
    n = len(nums)
    if n == 0:
        return 0
    l = 0
    u = n - 1

    if target < nums[l]:
        return l
    if target > nums[u]:
        return u + 1

    while l <= u:
        mid = (l + u) // 2
        if target == nums[mid]:
            return mid
        else:
            if target > nums[mid]:
                l = mid
            else:
                u = mid
            if u - l == 1:
                return u


if __name__ == '__main__':
    matrix = \
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
    print(search_matrix(matrix, 5))
    print(search_matrix(matrix, 20))
