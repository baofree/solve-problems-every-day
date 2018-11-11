"""
Given a string and an integer k,
you need to reverse the first k characters for every 2k characters counting from the start of the string.
If there are less than k characters left, reverse all of them.
If there are less than 2k but greater than or equal to k characters,
then reverse the first k characters and left the other as original.

Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]


"""


class Solution:

    def reverse(self, s):
        for index in range(int(len(s) / 2)):
            temp = s[index]
            s[index] = s[len(s) - 1 - index]
            s[len(s) - 1 - index] = temp
        return s

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)

        for index in range(0, len(s), k * 2):
            s[index:index + k] = self.reverse(s[index:index + k])

        return ''.join(s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseStr('abcdefg', 2))  # bacdfeg
    print(solution.reverseStr("abcdef", 3))  # cbadef
