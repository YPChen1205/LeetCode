def has_cycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head is None:
        return False

    slower = head
    faster = head.next

    while slower and faster and faster.next:
        if slower == faster:
            return True
        slower = slower.next
        faster = faster.next.next
    return False


if __name__ == '__main__':
    import linked_list as llst

    llist1 = llst.LinkedList.create_llist([3, 2, 0, -4])

    p = llist1
    while p:
        last = p
        p = p.next

    last.next = llist1.next

    print(has_cycle(llist1))
