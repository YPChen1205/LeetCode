def my_sqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x <= 1:
        return x
    l = 1
    h = x
    while l <= h:
        m = l + (h-l)//2
        sq = x//m
        if sq == m:
            return m
        elif m > sq:
            h = m - 1
        else:
            l = m + 1
    return h


if __name__ == '__main__':
    print(my_sqrt(8))