def num_squares(n):
    """
    :type n: int
    :rtype: int
    """
    square_list = gen_squares(n)
    dp = [0 for i in range(n + 1)]
    for i in range(n + 1):
        minimum = n + 1
        for square in square_list:
            if square > i:
                break
            minimum = min(minimum, dp[i - square] + 1)
            dp[i] = minimum
    return dp[n]


def gen_squares(n):
    square_list = []
    diff = 3
    square = 1
    while square <= n:
        square_list.append(square)
        square += diff
        diff += 2
    return square_list


if __name__ == '__main__':
    print(num_squares(12))
    print(num_squares(13))
