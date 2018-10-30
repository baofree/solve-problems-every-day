"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""
import re


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        str_list = s.strip().split(' ')

        last_word = str_list[-1]
        if re.fullmatch(r'([A-Z]|[a-z])+', last_word):
            return len(last_word)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLastWord('a '))
    print(solution.lengthOfLastWord('Hello world'))
    print(solution.lengthOfLastWord('Hello world1'))
    print(solution.lengthOfLastWord('Hello World'))
    print(solution.lengthOfLastWord('Hello Wor1ld'))
    print(solution.lengthOfLastWord('Hello WORLD'))
    print(solution.lengthOfLastWord('Hello WORL!D'))
    print(solution.lengthOfLastWord('Hello World1'))
