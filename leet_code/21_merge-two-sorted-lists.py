"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
from leet_code import helper


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = helper.ListNode(0)
        l3 = dummy
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        if l1 is not None:
            l3.next = l1
        if l2 is not None:
            l3.next = l2
        return dummy.next

    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = []
        while l1 or l2:
            a = l1.val if l1 else None
            b = l2.val if l2 else None
            if a is None:
                result.append(b)
                if l2:
                    l2 = l2.next
                continue
            elif b is None:
                result.append(a)
                if l1:
                    l1 = l1.next
                continue

            if a <= b:
                result.append(a)
                if l1:
                    l1 = l1.next
                continue
            else:
                result.append(b)
                if l2:
                    l2 = l2.next
                continue
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.mergeTwoLists(helper.gen_linked_list([1, 2, 4]), helper.gen_linked_list([1, 3])))
    # print(solution.mergeTwoLists(helper.gen_linked_list([1, 2, 4]), helper.gen_linked_list([1, 3, 4])))
