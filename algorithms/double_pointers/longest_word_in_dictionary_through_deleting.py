def find_longest_word(s, d):
    """
    :type s: str
    :type d: List[str]
    :rtype: str
    """
    max = 0
    res = ''
    for w in d:
        if is_in(s, w):
            if len(w) > max:
                max = len(w)
                res = w
            if len(w) == max:
                if w < res:
                    res = w
    return res


def is_in(s, w):
    i = 0
    j = 0
    while i < len(s) and j < len(w):
        if s[i] != w[j]:
            i += 1
        else:
            i += 1
            j += 1
    if j == len(w) and s[i-1] == w[j-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    s = "abpcplea"
    d = ["ale", "apple", "monkey", "plea"]
    print(find_longest_word(s, d))

    s = "abpcplea"
    d = ["a", "b", "c"]
    print(find_longest_word(s, d))
