def find_error_nums(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    map = {}
    n = len(nums)
    for i in nums:
        if i in map:
            map[i] += 1
            dup = i
        else:
            map[i] = 1

    ori = {i for i in range(1,n)}
    mis = ori - set(nums)

    return [dup, mis.pop()]

if __name__ == '__main__':
    print(find_error_nums([1,2,2,4]))
