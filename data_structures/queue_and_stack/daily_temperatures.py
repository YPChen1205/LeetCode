def daily_temperatures(T):
    """
    :type T: List[int]
    :rtype: List[int]
    """
    last_idx = len(T)-1
    stack = [[last_idx,T[-1]]]
    res = [0 for i in T]
    for i in range(last_idx-1,-1,-1):
        while stack:
            if T[i] < stack[-1][1]:
               res[i] = stack[-1][0] - i
               stack.append([i,T[i]])
               break
            else:
               stack.pop()
        if not stack:
            stack.append([i, T[i]])
    return res

if __name__ == '__main__':
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))

