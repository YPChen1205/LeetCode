def erase_overlap_intervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    ans = 0
    if not intervals:
        return ans
    intervals = sorted(intervals, key=lambda i: i[1])  # sort according the last number
    end = intervals[0][1]
    for intv in intervals[1:]:
        if intv[0] < end: # if overlaped, then it should be deleted
            ans += 1
            continue
        end = intv[1]
    return ans


if __name__ == '__main__':
    print(erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]))
    print(erase_overlap_intervals([[1, 2], [2, 3]]))
