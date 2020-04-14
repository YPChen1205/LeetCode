def search_range(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    res = [-1, -1]
    first = bin_search_first_position(nums, target)
    last = bin_search_first_position(nums, target + 1) - 1
    if nums[first] == target:
        res[0] = first
        res[1] = last
    return res


def bin_search_first_position(nums, t):
    l = 0
    h = len(nums) - 1
    while l < h:
        m = l + (h - l) // 2
        if nums[m] < t:
            l = m + 1
        else:
            h = m
    return l


if __name__ == '__main__':
   print(search_range([5,7,7,8,8,10], 8))
   print(search_range([5,7,7,8,8,10], 6))