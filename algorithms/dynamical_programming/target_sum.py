# idea: sum(P) - sum(N) = target  => 2 * sum(P) = target + sum(nums)
def find_target_sum_ways(nums, s):
    """
    :type nums: List[int]
    :type s: int
    :rtype: int
    """
    nums_sum = sum(nums)
    if (nums_sum + s) % 2 == 1 or nums_sum < s:
        return 0
    w = int((nums_sum + s) / 2)
    dp = [0 for i in range(w + 1)]
    dp[0] = 1

    for n in nums:
        for i in range(w, n - 1, -1):
            dp[i] = dp[i] + dp[i - n]
    return dp[w]


if __name__ == '__main__':
    print(find_target_sum_ways([1, 1, 1, 1, 1], 3))
