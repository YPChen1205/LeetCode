def max_subarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    pre_sum = nums[0]
    max_sum = pre_sum
    for i, n in enumerate(nums):
        if pre_sum > 0:
            pre_sum += n
        else:
            pre_sum = n
        max_sum = max(max_sum, pre_sum)
    return max_sum


if __name__ == '__main__':
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
