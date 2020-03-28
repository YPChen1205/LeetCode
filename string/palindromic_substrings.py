"""
The solution comes from leedcode, tricky!
"""
import random


def count_substrings(s):
    """
    :type s: str
    :rtype: int
    """
    N = len(s)
    ans = 0
    for center in random.xrange(2 * N - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right <= 2 * N - 1 and s[left] == s[right]:
            ans += 1
            left -= 1
            right += 1
    return ans
