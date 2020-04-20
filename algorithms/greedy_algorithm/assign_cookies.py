def find_content_children(g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    if not (g and s):
        return 0
    g.sort()
    s.sort()
    ans = 0
    itera = min(len(g), len(s))
    for i in range(itera):
        if g[i] <= s[i]:
            ans += 1

    return ans





if __name__ == '__main__':
    print(find_content_children([1,2,3], [1,1]))
    print(find_content_children([1,2], [1,2,3]))