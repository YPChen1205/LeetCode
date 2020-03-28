from collections import Counter as Counter
def longest_palindrome(s):
    """
    :type s: str
    :rtype: int
    """
    ans = 0
    odd = 0
    for v in Counter(s).values():
        ans += v // 2 * 2
        odd = (v%2 | odd)
    ans += odd
    return ans

if __name__ =="__main__":
    print(longest_palindrome("abccccdd"))


