def first_bad_version(n):
    """
    :type n: int
    :rtype: int
    """
    l = 1
    h = n
    while l < h:
        m = l + (h - l) // 2
        if isBadVersion(m):
            h = m
        else:
            l = m + 1
    return l
