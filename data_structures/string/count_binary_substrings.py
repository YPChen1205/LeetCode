"""
Idea：straitforward implementation, more clever solution is using group(refer to Leetcode)
"""
def count_binary_substrings(s):
    """
    :type s: str
    :rtype: int
    """
    res = 0
    str_len = len(s)
    for (idx, c) in enumerate(s):
        change, count1, count2 = 0, 1, 0
        for i in range(idx+1, str_len):
            if s[i] == s[i-1]:
                if change == 0:
                    count1 += 1
                if change == 1:
                    count2 += 1
                # this case is th
                if count2 == count1:
                    res += 1
                    break
            else:
                change += 1
                if change == 1:
                    count2 += 1
                    if count1 == count2:
                        res += 1
                        break
                if change == 2:
                    break
    return res


if __name__ == "__main__":
    print(count_binary_substrings("00110011"))
    print(count_binary_substrings("10101"))