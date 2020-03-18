def longestCommonPrefix(strs):
    """"
    :type strs: List[str]
    :type: str
    """
    common = strs[0]
    for i in range(1,len(strs)):
        checkstr = strs[i]
        checklen = min(len(common), len(checkstr))
        for j in range(checklen):
            if (common[j] != checkstr[j]):
                break
    common = common[:j]
    print(common)

