'''

'''


def reverse_list_iter(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    cur = head
    pre = None
    while cur is not None:
        tem = pre
        pre = cur
        cur = cur.next
        pre.next = tem
    return pre


def reverse_list_recursive(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head.next == None or head == None:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


if __name__ == "__main__":
    import linked_list as llist
    llst1 = llist.LinkedList.create_llist([1,2,3,4,5])
    llist.LinkedList.print_llst(reverse_list_iter(llst1))
    llist.LinkedList.print_llst(reverse_list_recursive(llst1))