def get_sum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    if b:
        return get_sum((a^b), (a&b)<<1)
    return a

if __name__ == '__main__':
 print(get_sum(3,5))