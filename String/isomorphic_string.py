"""
The idea of this sollution is map different character to interger for each string
then compare the mapped value of them
"""
def is_isomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    res = False
    if len(s) == len(t): # not sure about if isomrphic string should have the same length
        if list(map(s)) == list(map(t)):
            res = True
    return res

def map(str):
    dic = dict()
    i = 0
    for c in str:
        if c not in dic:
            dic[c] = i
            i += 1
    return dic.values()

if __name__ == "__main__":
    print(is_isomorphic(s="egg", t ="add"))
    print(is_isomorphic( s = "foo", t = "bar"))
    print(is_isomorphic( s = "paper", t = "title"))
