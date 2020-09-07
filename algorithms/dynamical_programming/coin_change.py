def coin_change(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    dp = []
    for coin in coins:
        for i in range(coin, amount+1):
            if i == coin:
                dp[i] = 1
            elif dp[i] == 0 and dp[i-coin] != 0:
                dp[i] = dp[i-coin]+1
            elif dp[i-coin] != 0:
                dp[i] = min(dp[i], dp[i-coin]+1)
    if dp[amount]:
        return dp[amount]
    else:
        return -1