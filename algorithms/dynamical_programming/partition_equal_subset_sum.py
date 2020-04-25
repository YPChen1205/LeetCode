def can_partition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nsum = sum(nums)
    if nsum % 2 != 0: return False
    psum = int(nsum / 2)
    dp = [False for i in range(psum + 1)]
    dp[0] = True
    for n in nums:
        for i in range(psum, 0, -1):
            dp[i] = dp[i] or dp[i - n]
    return dp[psum]


if __name__ == '__main__':
    print(can_partition([1, 5, 11, 5]))  # True
    print(can_partition([1, 2, 3, 5]))  # False
