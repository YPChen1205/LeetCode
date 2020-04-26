from linked_list import ListNode


# brute force
def swap_pairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    node = ListNode(-1)
    node.next = head
    pre = node
    while pre.next and pre.next.next:
        l1 = pre.next
        l2 = pre.next.next
        nxt = l2.next
        l1.next = nxt
        l2.next = l1
        pre.next = l2
        pre = l1

    return node.next
