def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    for (i,c) in enumerate(s):
        if s[i+1:].find(c) == -1:
            return i



