def merge_two_lists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    if l1.val < l2.val:
        l1.next = merge_two_lists(l1.next,l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2

if __name__ == "__main__":
    import linked_list as llst
    l1 = llst.LinkedList.create_llist([1,2,4])
    l2 = llst.LinkedList.create_llist([1,3,4])
    llst.LinkedList.print_llst(merge_two_lists(l1,l2))
