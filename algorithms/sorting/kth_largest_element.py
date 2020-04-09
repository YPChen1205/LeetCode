"""The idenums is to use quick sort, time complexity: O(n) space complexity: O(1)"""


def find_kth_largest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    k = len(nums) - k
    left = 0
    right = len(nums) - 1
    while left < right:
        pos = partition(nums, left, right)
        if pos == k:
            break
        elif pos < k:
            left = pos + 1
        else:
            right = pos - 1
    return nums[k]


def partition(nums, l, r):
    """
    partition the list into two parts (smaller or greater than privot)
    return the poistion of privot
    """
    i = l
    j = r
    pivot = nums[l]  # leftmost element as pivot
    while True:
        while nums[i] <= pivot and i < r:
            i += 1
        while nums[j] > pivot and j > l:
            j -= 1
        if i >= j:
            break
        swap(nums, i, j)
    swap(nums, l, j)
    return j


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))
    print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
