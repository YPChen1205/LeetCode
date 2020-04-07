def valid_palindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    i = 0
    j = len(s)-1
    while i < j:
        if s[i] != s[j]:
            return is_palindrome(s,i,j-1) or is_palindrome(s,i+1,j)
        else:
            i += 1
            j -= 1
    return True



def is_palindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j += 1
    return True




if __name__ == '__main__':
    print(valid_palindrome('aba'))
    print(valid_palindrome('abca'))
    print(valid_palindrome('abcea'))