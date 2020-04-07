"Idea: using two pointer that make sure the gap between them is n"
def remove_nth_from_end(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    gap = 0
    slower = faster = head
    while faster.next:
        gap += 1
        faster = faster.next
        if gap > n: # insure the gap between slower pointer and faster pointer
            slower = slower.next
    if gap == n-1:
        return head.next
    else:
        slower.next = slower.next.next
        return head


if __name__ == "__main__":
    import linked_list as llst
    head = llst.LinkedList.create_llist([1,2,3,4,5])
    llst.LinkedList.print_llst(remove_nth_from_end(head, 2))