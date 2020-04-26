from linked_list import LinkedList


def split_list_to_parts(root, k):
    """
    :type root: ListNode
    :type k: int
    :rtype: List[ListNode]
    """
    node = root
    cnt = 0
    while node:
        cnt += 1
        node = node.next

    width, rem = divmod(cnt, k)

    ans = []
    cur = root
    for i in range(k):
        head = cur
        for j in range(width + (i < rem)-1):  # interesting coding
            if cur: cur = cur.next
        if cur:
            cur.next, cur = None, cur.next
        ans.append(head.val)
    return ans


if __name__ == '__main__':
    root = LinkedList.create_llist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(split_list_to_parts(root, 3))
