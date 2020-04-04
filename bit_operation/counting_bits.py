def count_bits(num):
    """
    :type num: int
    :rtype: List[int]
    """
    res = [0 for i in range(num+1)]
    for i in range(1, num+1):
        res[i] = res[i&(i-1)]+1
    return res


if __name__ == '__main__':
    print(count_bits(2))
    print(count_bits(5))