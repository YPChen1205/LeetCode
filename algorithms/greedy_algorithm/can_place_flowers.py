def can_place_flowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type bed_len: int
    :rtype: bool
    """
    bed_len = len(flowerbed)
    cnt = 0
    for i, f in enumerate(flowerbed):
        if f:
            continue
        pre_empty = True
        nxt_empty = True
        if (i == 0 and flowerbed[i] == 1) or (i > 0 and flowerbed[i - 1] == 1):
            pre_empty = False
        if i < bed_len - 1 and flowerbed[i + 1] == 1:
            nxt_empty = False
        if pre_empty and nxt_empty:
            cnt += 1
    return cnt >= n


if __name__ == '__main__':
    print(can_place_flowers([1, 0, 0, 0, 1], 1))
    print(can_place_flowers([1, 0, 0, 0, 1], 2))
