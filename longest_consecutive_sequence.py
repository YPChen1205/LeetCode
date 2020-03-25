"""
The idea of the solution is use map, because in map search for one element cost O(1)

"""
def longest_consecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums_set = set(nums)
    max_len = 0
    for i in nums_set:
        cons_len = 1
        j = i + 1
        while j in nums_set:
            cons_len += 1
            j += 1

        if max_len < cons_len:
            max_len = cons_len
    return max_len

if __name__ == '__main__':
   print(longest_consecutive([100, 4, 200, 1, 3, 2]))