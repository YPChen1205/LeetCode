import collections
import heapq
def top_k_frequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    count = collections.Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)


if __name__ == '__main__':
    print(top_k_frequent(nums=[1, 1, 1, 2, 2, 3], k=2))
