def wiggle_max_length(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    up = 1
    down = 1
    for i, n in enumerate(nums):
        if i == 0:
            continue
        if nums[i] < nums[i - 1]:
            down = up + 1
        if nums[i] > nums[i - 1]:
            up = down + 1
    return max(up, down)


if __name__ == '__main__':
    print(wiggle_max_length([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
    print(wiggle_max_length([1,2,3,4,5,6,7,8,9]))
    print(wiggle_max_length([1,7,4,9,2,5]))