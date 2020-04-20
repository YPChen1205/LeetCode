# House Robber I
def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    house_num = len(nums)
    dp = [0 for n in nums]
    dp[0] = nums[0]
    dp[1] = nums[1]
    for i in range(2, house_num):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    return dp[house_num - 1]


# House Robber II
def rob2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not (nums and len(nums)):
        return 0
    house_num = len(nums)

    def rob_range(nums, first, last):
        pre2 = 0
        pre1 = 0
        for i in range(first, last):
            cur = max(pre1, pre2 + nums[i])
            pre2 = pre1
            pre1 = cur
        return cur

    return max(rob_range(nums, 0, house_num - 1), rob_range(nums, 1, house_num))


if __name__ == '__main__':
    print(rob([2, 7, 9, 3, 1]))

    print(rob2([2, 3, 2]))
    print(rob2([1, 2, 3, 1]))
