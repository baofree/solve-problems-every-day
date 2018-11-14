"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

"""
from functools import reduce


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_list = list(str(num))
        if len(num_list) == 1:
            return num
        return self.addDigits(reduce(lambda a, b: int(a) + int(b), num_list))

    def addDigits2(self, num):
        return 1 + (num - 1) % 9


if __name__ == '__main__':
    solution = Solution()
    print(solution.addDigits(38))
    print(solution.addDigits2(38))
