"""
Given a positive integer num, write a function which returns True
if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Output: true

Example 2:
Input: 14
Output: false


"""


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for i in range(num + 1):
            if i * i == num:
                return True
            elif i * i > num:
                return False
        return False

    def isPerfectSquare2(self, num):
        left = 0
        right = num
        while left <= right:
            mid = left + (right - left) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPerfectSquare(16))
    print(solution.isPerfectSquare(14))
    print(solution.isPerfectSquare2(16))
    print(solution.isPerfectSquare2(14))
