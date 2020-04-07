def reverse_vowels(s):
    """
    :type s: str
    :rtype: str
    """
    p1 = 0
    p2 = len(s) - 1
    vowel = {'a', 'e', 'i', 'o', 'u'}
    while p1 < p2:
        if s[p1] in vowel:
            if s[p2] in vowel:
                temp = s[p1]
                s_first = s[:p1]
                s_second = s[p1+1:]
                s = s_first + s[p2] + s_second
                s_first = s[:p2]
                s_second = s[p2+1:]
                s = s_first + temp + s_second
                p1 += 1
                p2 -= 1
            else:
                p2 -= 1
        elif s[p2] in vowel:
            p1 += 1
        else:
            p1 += 1
            p2 -= 1

    return s


if __name__ == '__main__':
    print(reverse_vowels('hello'))
    print(reverse_vowels('leetcode'))
