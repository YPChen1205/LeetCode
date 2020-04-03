def find_complement(num):
    """
    :type num: int
    :rtype: int
    """
    b = bin(num)
    mask = int('0' * (30 - len(b)) + '1' * (len(b)-2), 2)
    return num ^ mask


if __name__ == '__main__':
    print(find_complement(5))
    print(find_complement(1))
