class LinkedList:
    def __init__(self):
        self.head = None
        pass

    def add(self, val):
        if not self.head:
            self.head = ListNode(val)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = ListNode(val)


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def gen_linked_list(input_list):
    linked_list = LinkedList()

    for input_val in input_list:
        linked_list.add(input_val)
    return linked_list.head
