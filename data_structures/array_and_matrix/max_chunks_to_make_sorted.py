def max_chunks_to_sorted(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    ans = ma = 0
    for i, x in enumerate(arr):
        ma = max(ma, x)
        if ma == i:
            ans += 1
    return ans

if __name__ == '__main__':
    print(max_chunks_to_sorted([2,3,4,1,0]))