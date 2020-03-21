def three_sum(num):
    """"
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    sollution = []
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            for k in range((j+1),len(num)):
                if (num[i]+num[j]+num[k] == 0):
                    case = [num[i], num[j], num[k]]
                    case.sort()
                    if case not in sollution:
                        sollution.append(case)
    print(sollution)


