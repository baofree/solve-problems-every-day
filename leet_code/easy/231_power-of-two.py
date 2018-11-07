"""
Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true
Explanation: 20 = 1

Example 2:
Input: 16
Output: true
Explanation: 24 = 16

Example 3:
Input: 218
Output: false


"""


class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 0
        while True:
            if 2 ** i == n:
                return True
            if 2 ** i > n:
                break
            i += 1
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfTwo(1))
    print(solution.isPowerOfTwo(16))
    print(solution.isPowerOfTwo(218))
