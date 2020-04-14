def next_greatest_letter(letters, target):
    """
    :type letters: List[str]
    :type target: str
    :rtype: str
    """
    l = 0
    h = len(letters) - 1

    if target > letters[-1]:
        return letters[0]
    while l <= h:
        m = l + (h - l) // 2
        if m > target:
            h = m - 1
        else:
            l = m + 1

    return letters[l]
