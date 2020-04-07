def get_sum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """

    if b == 0:
        return a
    else:
        return get_sum(a ^ b, (a & b) << 1)
    print("a: %s, b: %s" % (bin(~a), bin(b)))





if __name__ == '__main__':
    # print(get_sum(1, 2))
    print(get_sum(-2, 3))
