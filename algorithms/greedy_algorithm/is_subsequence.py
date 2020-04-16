def is_subsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    idx = -1
    for c in s:
        idx = t[(idx+1):].find(c)
        if idx == -1:
            return False
    return True



if __name__ == '__main__':
    print(is_subsequence(s = "abc", t = "ahbgdc"))
    print(is_subsequence(s = "axc", t = "ahbgdc"))