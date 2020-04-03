def is_power_of_four(n):
    """
    :type n: int
    :rtype: bool
    """
    return n > 0 and (n & (n - 1) == 0) and (n & int('1000'*8) == 0)


if __name__ == '__main__':
    print(is_power_of_four(5))
    print(is_power_of_four(16))