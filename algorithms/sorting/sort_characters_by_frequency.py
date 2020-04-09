import collections


def frequency_sort(s):
    """
    :type s: str
    :rtype: str
    """
    c = collections.Counter(s)
    sorted_counter = sorted(c.items(), key=lambda i: i[1], reverse=True)
    return ''.join([i[0] * i[1] for i in sorted_counter])


if __name__ == '__main__':
    print(frequency_sort("tree"))
