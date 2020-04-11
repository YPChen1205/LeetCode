def num_squares(n):
    """
    :type n: int
    :rtype: int
    """
    squres = gen_squares(n)
    queue = [n]
    marked = [False for i in range(n + 1)]
    marked[n] = True
    level = 0
    while queue:
        queue_len = len(queue)
        level += 1
        while queue_len > 0:
            cur = queue[0]
            queue.pop(0)
            queue_len -= 1
            for s in squres:
                next = cur - s
                if next < 0:
                    break
                if next == 0:
                    return level
                if marked[next]:
                    continue
                marked[next] = True
                queue.append(next)
    return n


def gen_squares(n: int):
    """
    generate all squares less equal than the number n
    :param n:
    :return: list
    """
    squares = []
    square = 1
    diff = 3
    while square <= n:
        squares.append(square)
        square += diff
        diff += 2
    return squares


if __name__ == '__main__':
    print(num_squares(12))
    print(num_squares(13))
