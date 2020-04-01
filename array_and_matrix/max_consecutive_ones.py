def find_max_consecutive_ones(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cur = maxi = 0

    # important, use as stopword for counting
    if nums[-1] == 1:
        nums.append(0)

    for i in nums:
        if i == 1:
            cur += 1
        else:
            if cur > maxi:
                maxi = cur
            cur = 0
    return maxi


if __name__ == '__main__':
    print(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]))
