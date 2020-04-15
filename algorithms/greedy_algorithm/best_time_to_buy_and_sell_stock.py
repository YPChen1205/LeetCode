def max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0
    min_price = prices[0]
    ans = 0
    for p in prices:
        if p < min_price:
            min_price = p
        else:
            ans = max(ans, p - min_price)
    return ans


def advanced_max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0
    ans = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            ans += (prices[i] - prices[i - 1])
    return ans


if __name__ == '__main__':
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
    print(max_profit([7, 6, 4, 3, 1]))  # 0

    print(advanced_max_profit([7, 1, 5, 3, 6, 4]))  # 7
    print(advanced_max_profit([1, 2, 3, 4, 5]))  # 4
    print(advanced_max_profit([7, 6, 4, 3, 1]))  # 0
