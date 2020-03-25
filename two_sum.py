'''
The idea of this sollution is intuitive
just using two for-loop search, trick is the second loop is start from i
to avoid repeating calling the former elements
'''
def two_sum(nums, target):
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
    two_sum([2, 7, 11, 15], 9)