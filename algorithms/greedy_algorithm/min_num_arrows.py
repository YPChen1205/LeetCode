def find_min_arrow_shots(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    if not points:
        return 0
    points = sorted(points, key=lambda i: i[1])
    ans = 1
    end = points[0][1]
    for p in points:
        if p[0] <= end:
            continue
        ans += 1
        end = p[1]
    return ans


if __name__ == '__main__':
    print(find_min_arrow_shots([[10, 16], [2, 8], [1, 6], [7, 12]]))
