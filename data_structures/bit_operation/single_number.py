def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = nums[0]
    for i in nums[1:]:
       a ^= i
    return a


if __name__ == '__main__':
    print(single_number([2, 2, 1]))
    print(single_number([4, 1, 2, 1, 2]))
