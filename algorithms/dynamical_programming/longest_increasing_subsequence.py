def length_of_LIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ln = len(nums)
    dp = [1 for n in nums]
    for i in range(1, ln):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


if __name__ == '__main__':
    print(length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18]))
