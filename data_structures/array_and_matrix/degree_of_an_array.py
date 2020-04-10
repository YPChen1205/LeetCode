import collections


def find_shortest_subarray(nums: list):
    """
    :type nums: List[int]
    :rtype: int
    """
    left, right, count = {}, {}, {}
    for i, n in enumerate(nums):
        if n not in left:
            left[n] = i
        right[n] = i
        count[n] = count.get(n, 0) + 1

    ans = len(nums)
    degree = max(count.values())
    for n in count:
        if count[n] == degree:
            ans = min(right[n] - left[n] + 1, ans)
    return ans


if __name__ == '__main__':
    print(find_shortest_subarray([1, 2, 2, 3, 1, 4, 2]))
