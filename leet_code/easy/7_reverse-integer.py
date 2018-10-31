"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the
32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x_list = list(str(abs(x)))
        x_list.reverse()
        ret_str = ''.join(x_list)
        ret = sign * int(ret_str)
        if -2 ** 31 > ret or 2 ** 31 - 1 < ret:
            return 0
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(123))  # 321
    print(solution.reverse(-123))  # -321
    print(solution.reverse(120))  # 21
    print(solution.reverse(1534236469))  # 9646324351 -> 0
    print(solution.reverse(1563847412))  # 2147483651
