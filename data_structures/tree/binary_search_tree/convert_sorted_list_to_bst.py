from tree import TreeNode


def sorted_list_to_bst(head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    if not head:
        return None
    if not head.next:
        return TreeNode(head.val)
    pre_mid = _pre_mid(head)
    mid = pre_mid.next
    pre_mid.next = None
    t = TreeNode(mid.val)
    t.left = sorted_list_to_bst(head)
    t.right = sorted_list_to_bst(mid.next)
    return t


def _pre_mid(head):
    slow = head
    fast = head.next
    pre = head
    while fast and fast.next:
        pre = slow
        slow = slow.next
        fast = fast.next.next
    return pre
