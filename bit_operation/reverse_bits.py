def reverse_bits(n):
    """
    :param n: int
    :return: int
    """
    b = bin(n)[:1:-1]  # reverse why??
    return int(b + '0' * (32 - len(b)), 2)


if __name__ == '__main__':
    print(reverse_bits(8))