def sort_colors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    zero = -1
    one = 0
    two = len(nums)

    while one < two:
        if nums[one] == 0:
            zero += 1
            swap(nums, zero, one)  # important step
            one += 1
        elif nums[one] == 2:
            two -= 1
            swap(nums, one, two)
        else:
            one += 1
    return nums


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    print(sort_colors([2, 0, 2, 1, 1, 0]))
