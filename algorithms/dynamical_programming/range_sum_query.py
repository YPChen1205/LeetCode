def sum_range(nums, i, j):
    """
    :type i: int
    :type j: int
    :rtype: int
    """
    return sum(nums[:j + 1]) - sum(nums[:i])


if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    print(sum_range(nums, 0, 2))
    print(sum_range(nums, 2, 5))
    print(sum_range(nums, 0, 5))
