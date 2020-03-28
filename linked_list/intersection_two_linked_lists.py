"""
Idea:  2-pointers, very tricky! details refer to leedcode solution
"""
def get_intersection_node(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    p_A = headA
    p_B = headB

    while p_A != p_B:
        if p_A == None:
            p_A = headB
        else:
            p_A = p_A.next

        if p_B == None:
            p_B = headA
        else:
           p_B =  p_B.next

    return p_A


if __name__ == "__main__":
    import linked_list as llst
    common = llst.LinkedList.create_llist([8, 4, 5])
    h1 = llst.LinkedList.create_llist([4, 1])
    h2 = llst.LinkedList.create_llist([5, 0, 2])
    headA = llst.LinkedList.join_two_llists(h1, common)
    headB = llst.LinkedList.join_two_llists(h2, common)
    # llst.LinkedList.print_llst(headA)
    # llst.LinkedList.print_llst(headB)

    print(get_intersection_node(headA,headB).val)
