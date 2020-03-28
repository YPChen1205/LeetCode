
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create_llist(lst):
        llst = LinkedList()
        llst.head = ListNode(lst[0])
        nodes = [llst.head]
        for i in lst[1:]:
            cur_node = ListNode(i)
            nodes.append(cur_node)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        list_head = nodes[0]
        return list_head

    def join_two_llists(llst1, llst2):
        """
        concatenate the linklist 2 to linked list 1
        :param  llst1 llst2: ListNode
        :return: ListNode

        """
        pointer = llst1
        while pointer is not None:
            last_node = pointer
            pointer = pointer.next
        last_node.next = llst2
        return llst1

        return llst1

    def print_llst(llst):
        """
        :type: llist: Linked List
        :return: values of the linkedlist
        """
        pointer = llst
        print("List:")
        while pointer is not None:
            print(pointer.val)
            pointer = pointer.next
