def restore_ip_addresses(s):
    """
    :type s: str
    :rtype: List[str]
    """

    def backtrack(cnt, temp_add, res, s):
        if cnt == 4 or len(s) == 0:
            if cnt == 4 and len(s) == 0:
                res.append(temp_add)
            return
        for i in range(len(s)):
            if i == 0 and s[0] == '0' or i > 2:
                break
            part = s[:i + 1]
            if int(part) <= 255:
                if len(temp_add):
                    part = "." + part
                temp_add += part
                backtrack(cnt + 1, temp_add, res, s[i + 1:])
                temp_add = temp_add[:(len(temp_add) - len(part))]

    res = []
    backtrack(0, '', res, s)
    return res


if __name__ == '__main__':
    print(restore_ip_addresses("25525511135"))
