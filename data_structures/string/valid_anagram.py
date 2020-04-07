"The idea of  the solution is use hasmap"
def is_anagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    res = False
    if len(s)==len(t):
        dic1 = {c: s.count(c) for c in s}
        dic2 = {c: s.count(c) for c in t}
        if dic1 == dic2:
            res = True
    return res


if __name__ == '__main__':
    print(is_anagram( s = "rat", t = "car"))
    print(is_anagram(s="anagram", t = "nagaram"))