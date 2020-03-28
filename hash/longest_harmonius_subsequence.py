'''The idea of this solution is use map(in python dic, where key = element, value = count(elemnt)
'''
def find_LHS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dic = {}
    for e in nums:
        if e in dic:
            dic[e] += 1
        else:
            dic[e] = 1

    max_len = 0
    for i in dic.keys():
        if i+1 in dic.keys():
            add_len = dic[i]+dic[i+1]
        else:
            add_len = dic[i]
        if max_len < add_len:
            max_len = add_len

    return max_len
if __name__ == "__main__":
    print(find_LHS([1,3,2,2,5,2,3,7]))