def next_greater_element(nums):
    """
     :type nums: List[int]
     :rtype: List[int]
     """
    n = len(nums)
    res = [-1 for i in nums]
    stack = []
    for i in range(2*n):
        num = nums[i%n]
        while stack and nums[stack[-1][0]]<num:
            res[stack[-1][0]] = num
            stack.pop()
        if i < n:
            stack.append([i,nums[i]])

    return res


if __name__ == '__main__':
    print(next_greater_element([73, 74, 75, 71, 69, 72, 76, 73]))