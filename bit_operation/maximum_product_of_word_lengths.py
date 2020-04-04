def max_product(words):
    """
    :type words: List[str]
    :rtype: int
    """
    res = 0
    n = len(words)
    for i in range(n):
        for j in range(i + 1, n):
            if bit_map(words[i]) & bit_map(words[j]) == 0:  # only there is no overlap in character the result will be 0
                res = max(res, len(words[i]) * len(words[j]))
    return res


def bit_map(word):
    """
    map the character in a word to bit, different characters are in different bits
    :param word: str
    :return: int
    """
    c_bit = 0
    for c in word:
        c_bit |= (1 << (ord(c) - ord('a')))
    return c_bit


if __name__ == '__main__':
    print(max_product(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
    print(max_product(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
    print(max_product(["a", "aa", "aaa", "aaaa"]))
