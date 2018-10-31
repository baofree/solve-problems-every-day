from leet_code import helper


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        result = []
        while pre:
            result.append(pre.val)
            pre = pre.next
        return result

    def reverseList1(self, head):
        if head is None or head.next is None:
            return head
        node = self.reverseList1(head.next)
        head.next.next = head
        head.next = None
        return node


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseList(helper.gen_linked_list([1, 2, 3, 4, 5])))
    print(solution.reverseList1(helper.gen_linked_list([1, 2, 3, 4, 5])))
