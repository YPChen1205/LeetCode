def hamming_distance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    z = x ^ y
    cnt = 0
    while z != 0:
        if z & 1 == 1:
            cnt += 1
        z = z >> 1
    return cnt


if __name__ == '__main__':
    print(hamming_distance(1,4))
