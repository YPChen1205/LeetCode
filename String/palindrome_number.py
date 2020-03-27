"""
Idea: simple reversed the number
"""
def is_palindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    if x < 10:
        return True
    res = x
    rev = 0
    while res > 9:
        rem = res%10
        rev = (rev+rem) * 10
        res //= 10
    rev += res
    # print("original number: %s\nreversed numer: %s" %(x, rev))
    if rev == x:
        return True
    else:
        return False


if __name__ == "__main__":
    print(isPalindrome(121))
    print(isPalindrome(-121))
    print(isPalindrome(10))


