def single_non_duplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = 0
    h = len(nums) - 1
    while l < h:
        m = l + (h - l) // 2
        if m % 2 == 1:
            m -= 1  # ensure m in the even index
        if nums[m] == nums[m + 1]:
            l = m + 2  # if equal, means low parts are all pairs
        else:
            h = m
    return nums[l]

