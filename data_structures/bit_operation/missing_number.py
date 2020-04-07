def missing_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = len(nums)
    for i, num in enumerate(nums):
        a ^= (i ^ num)
    return a


if __name__ == '__main__':
    print(missing_number([3,0,1]))
    print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
