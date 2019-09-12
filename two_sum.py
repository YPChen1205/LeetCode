def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i] + nums[j] == target:
                output = [i,j]
                print(output)
                return output

if __name__ == "__main__":
    twoSum([2, 7, 11, 15],9)