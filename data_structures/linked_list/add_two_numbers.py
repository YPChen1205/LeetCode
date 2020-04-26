from linked_list import ListNode


# idea: use stack
def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    def stack(node):
        stack = []
        while node:
            stack.append(node.val)
            node = node.next
        return stack

    l1_stack = stack(l1)
    l2_stack = stack(l2)
    head = ListNode(-1)
    carry = 0
    while l1_stack or l2_stack or carry:
        x = 0
        y = 0
        if l1_stack:
            x = l1_stack[-1]
            l1_stack.pop()
        if l2_stack:
            y = l2_stack[-1]
            l2_stack.pop()
        num_sum = x + y + carry
        node = ListNode(num_sum % 10)
        node.next = head.next  # critical
        head.next = node
        carry = num_sum // 10
    return head.next
