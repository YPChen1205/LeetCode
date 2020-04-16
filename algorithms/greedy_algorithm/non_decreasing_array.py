from ipython_genutils.py3compat import xrange


def check_possibility(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    p = None
    for i in xrange(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            if p:
                return False
            p = i
            return (not p) or p == 0 or p == len(nums) - 2 or nums[p - 1] <= nums[p + 1] or nums[p] < nums[p + 2]


if __name__ == '__main__':
    print(check_possibility([4, 2, 3]))  # T
    print(check_possibility([4, 2, 1]))  # F
