"""
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"

Example 2:
Input: -7
Output: "-10"

Note: The input will be in range of [-1e7, 1e7].

"""


class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = []
        sign = None
        if num < 0:
            sign = '-'
        num = abs(num)
        while True:
            remainder = num % 7
            num = num // 7
            result.insert(0, str(remainder))
            if num == 0:
                break
        if sign:
            result.insert(0, sign)
        return ''.join(result)

    def convertToBase7Recursion(self, num):
        if num < 0:
            return '-' + self.convertToBase7(-num)
        if num < 7:
            return str(num)
        return self.convertToBase7Recursion(num // 7) + str(num % 7)

    def convertToBase7_2(self, num):
        if num == 0:
            return '0'
        n, res = abs(num), ''
        while n:
            res = str(n % 7) + res
            n //= 7
        return res if num > 0 else '-' + res


if __name__ == '__main__':
    solution = Solution()
    print(solution.convertToBase7(100))
    print(solution.convertToBase7(-7))

    print(solution.convertToBase7Recursion(100))
    print(solution.convertToBase7Recursion(-7))

    print(solution.convertToBase7_2(100))
    print(solution.convertToBase7_2(-7))
