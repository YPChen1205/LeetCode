"""
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
def find_duplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    tort = hare = nums[0]
    while(tort != hare):
        tort = nums[tort]
        hare = nums[nums[hare]]
    p1 = nums[0]
    p2 = tort
    while p1 != p2:
        p1 = nums[p1]
        p2 = nums[p2]
    return p1



if __name__ == '__main__':
    print(find_duplicate([1,3,4,2,2]))
    print(find_duplicate([3,1,3,4,2]))