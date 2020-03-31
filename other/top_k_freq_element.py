from collections import Counter

"""
The idea is quite intuitive
first count the number of all elements in the list
then return the most frequent k elements
"""
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    counter = Counter(nums)
    lst = list(set(counter.keys()))
    return lst[:k]


