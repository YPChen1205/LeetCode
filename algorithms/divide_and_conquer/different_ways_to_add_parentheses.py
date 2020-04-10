def diff_way_to_compute(input):
    """
    :type input: str
    :rtype: List[int]
    """
    ways = []
    for i, c in enumerate(input):
        if c in {'+', '-', '*'}:
            left = diff_way_to_compute(input[:i])
            right = diff_way_to_compute(input[i + 1:])
            for l in left:
                for r in right:
                    if c == '+':
                        ways.append(l + r)
                    if c == '-':
                        ways.append(l - r)
                    if c == '*':
                        ways.append(l * r)

    if len(ways) == 0:
        ways.append(int(input))
    return ways


if __name__ == '__main__':
    print(diff_way_to_compute("2*3-4*5"))
