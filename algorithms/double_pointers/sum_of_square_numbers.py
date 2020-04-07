import math


def judge_square_sum(c):
    """
    :type c: int
    :rtype: bool
    """
    if c < 0:
        return False
    r = math.sqrt(c)
    if math.floor(r) == r:
        return True
    s = 0
    b = math.floor(r)
    while s*s + b*b != c and s <= b:
        if s*s + b*b > c:
            b -= 1
        else:
            s += 1

    if b < s:
        return False
    else:
        return True


if __name__ == '__main__':
    print(judge_square_sum(5))
