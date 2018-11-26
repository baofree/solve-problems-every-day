"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?

"""


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num / 4 == 1 or num == 1:
            return True
        elif num / 4 < 1 or num % 4 != 0:
            return False
        return self.isPowerOfFour(num / 4)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfFour(0))
    print(solution.isPowerOfFour(1))
    print(solution.isPowerOfFour(4))
    print(solution.isPowerOfFour(5))
    print(solution.isPowerOfFour(16))
    print(solution.isPowerOfFour(5))
    print(solution.isPowerOfFour(16))
    print(solution.isPowerOfFour(64))
    print(solution.isPowerOfFour(66))
