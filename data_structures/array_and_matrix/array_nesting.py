def array_nesting(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    for i in range(len(nums)):
        cnt = 0
        j = i
        while nums[j] != -1:
            cnt += 1
            t = nums[j]
            nums[j] = -1
            j = t
        ans = max(ans, cnt)
    return ans


if __name__ == '__main__':
    print(array_nesting([5,4,0,3,1,6,2]))