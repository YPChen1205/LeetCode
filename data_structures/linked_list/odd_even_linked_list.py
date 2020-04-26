def odd_even_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    odd = head
    if not (odd and odd.next): return odd
    even = head.next
    even_head = even
    p = even # step last element
    while p.next:
        odd.next = odd.next.next
        odd = odd.next
        p = p.next
        if not p:
            break
        even.next = even.next.next
        even = even.next
        p = p.next
    odd.next = even_head

    return head

