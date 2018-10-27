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


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_bin_tree():
    data = [5, 4, 8, 11, 'null', 13, 4, 7, 2, 'null', 'null', 'null', 1]

    root = TreeNode(data[0])
    root.left = TreeNode(data[1])
    root.right = TreeNode(data[2])

    root.left.left = TreeNode(data[3])
    # root.left.right = TreeNode(input_list[4])
    root.right.left = TreeNode(data[5])
    root.right.right = TreeNode(data[6])

    root.left.left.left = TreeNode(data[7])
    root.left.left.right = TreeNode(data[8])

    root.right.right.right = TreeNode(data[12])

    return root
