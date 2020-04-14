def find_min(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l  = 0
    h = len(nums) - 1

    while l < h:
        m = l + (h-l)//2
        if nums[m] > nums[h]:
            l = m + 1
        else:
            h = m
    return nums[l]


if __name__ == '__main__':
    print(find_min([3,4,5,1,2] ))
    print(find_min([4,5,6,7,0,1,2]))




