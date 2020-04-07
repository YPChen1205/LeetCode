"The important thing is merge from back to front"
def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    i = m-1
    j = n-1
    k = m+n-1
    while i >= 0 or j >= 0:
        if i < 0:
            nums1[k] = nums2[j]
            j -= 1

        elif j < 0:
            nums1[k] = nums1[i]
            i -= 1

        elif nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    return nums1



if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(merge(nums1, m, nums2, n))
