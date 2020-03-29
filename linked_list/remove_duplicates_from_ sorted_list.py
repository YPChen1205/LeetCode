def delete_duplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head
    cur = head
    nxt = head.next
    while nxt is not None:
        while cur.val == nxt.val:
            nxt = nxt.next
        tmp = cur
        cur = nxt
        nxt = nxt.next
        tmp.next = cur
    return head


if __name__ == "__main__":
    import linked_list as llst

    head = llst.LinkedList.create_llist([1, 1, 1, 2, 2, 3, 4, 4])
    llst.LinkedList.print_llst(delete_duplicates(head))
