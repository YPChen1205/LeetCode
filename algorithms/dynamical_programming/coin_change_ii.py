def change(amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    if not coins:
        return 0
    dp = []
    dp[0]=1
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] += dp[i-coin]
    return dp[amount]