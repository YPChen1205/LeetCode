def number_of_arithmetic_slices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not (nums and len(nums)):
        return 0
    nums_len = len(nums)
    dp = [0 for n in nums]
    ans = 0
    for i in range(2, len(nums)):
        if nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]:
            dp[i] = dp[i - 1] + 1  # tricky
    ans = sum(dp)
    return ans


if __name__ == '__main__':
    print(number_of_arithmetic_slices([1, 2, 3, 4]))
