from linked_list import LinkedList
from reverse_linked_list import reverse_list_iter


def is_palindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    node = head
    cnt = 0
    while node:
        cnt += 1
        node = node.next

    head2 = head
    for i in range(int(cnt // 2)):
        head2 = head2.next
    if cnt % 2 == 1:
        head2 = head2.next
    head2 = reverse_list_iter(head2)

    while head2:
        if head.val != head2.val:
            return False
        head2 = head2.next
        head = head.next
    return True


if __name__ == '__main__':
    head = LinkedList.create_llist([1,2,3,1])
    print(is_palindrome(head))