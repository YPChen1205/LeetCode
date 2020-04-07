def two_sum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    s = 0
    b = len(numbers) - 1

    while numbers[s] + numbers[b] != target and s < b:
        if numbers[s] + numbers[b] > target:
            b -= 1
        if numbers[s] + numbers[b] < target:
            s += 1
    if s < b:
        return [s+1, b+1]
    else:
        return []


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))