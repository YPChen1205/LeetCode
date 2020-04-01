def move_zeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    last_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            if i - last_non_zero == 1 and last_non_zero != 0:  # pay attention when the first element == 0
                last_non_zero = i
            else:
                if nums[last_non_zero] != 0:
                    last_non_zero += 1
                nums[last_non_zero], nums[i] = nums[i], 0
    return nums


if __name__ == '__main__':
    print(move_zeroes([0, 1, 0, 3, 12]))
