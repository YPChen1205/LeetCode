def partition_labels(s):
    """
    :type s: str
    :rtype: List[int]
    """
    last = {c: i for i, c in enumerate(s)}
    print(last)
    j = anchor = 0
    ans = []
    for i, c in enumerate(s):
        j = max(j, last[c])
        if i == j:
            ans.append(i - anchor + 1)
            anchor = i + 1

    return ans


if __name__ == '__main__':
    print(partition_labels("ababcbacadefegdehijhklij"))  # [9,7,8]
