def single_number(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = [0,0]
    a = 0
    for i in nums:
        a ^= i
    diff = a^-a
    for i in nums:
        if (diff & i) == 0:
            res[0] ^= i
        else:
            res[1] ^= i
    return res


if __name__ == '__main__':
    print(single_number([1,2,1,3,2,5]))