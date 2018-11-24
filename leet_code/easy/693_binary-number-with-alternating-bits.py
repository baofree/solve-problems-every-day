"""
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101

Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.

Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.

Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.

"""


class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        time complexity : O(w)
        """
        old = 8
        while True:
            if n % 2 == old:
                return False
            old = n % 2
            n = n // 2
            if n < 1:
                break
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.hasAlternatingBits(0))
    print(solution.hasAlternatingBits(1))
    print(solution.hasAlternatingBits(2))
    print(solution.hasAlternatingBits(5))
    print(solution.hasAlternatingBits(7))
    print(solution.hasAlternatingBits(11))
    print(solution.hasAlternatingBits(10))
