"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?


"""

from leet_code import helper


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        queue = []

        while head:
            stack.append(head.val)
            queue.insert(0, head.val)
            head = head.next
        return stack == queue


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(helper.gen_linked_list([1, 2])))
    print(solution.isPalindrome(helper.gen_linked_list([1, 2, 2, 1])))
