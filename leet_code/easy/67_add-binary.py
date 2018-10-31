"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = list(a.zfill(len(b)))
        a.reverse()

        b = list(b.zfill(len(a)))
        b.reverse()

        result = []
        raising = 0
        for x, y in zip(a, b):
            sum_val = int(x) + int(y) + raising
            raising = int(sum_val / 2)
            result.append(str(sum_val % 2))
            # print(x, y, sum_val, sum_val % 2, int(sum_val / 2))
        if raising > 0:
            result.append('1')
        result.reverse()
        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary("11", "1"))  # "100"
    print(solution.addBinary("1010", "1011"))  # "10101"
