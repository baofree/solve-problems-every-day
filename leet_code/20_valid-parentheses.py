"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not (len(s) + 1) % 2:
            return False
        if not s:
            return True
        stack = []
        for sign in s:
            if sign in ['(', '[', '{']:
                stack.append(sign)
            else:
                if not stack:
                    return False
                before_sign = stack.pop()
                if sign == ')' and before_sign == '(':
                    pass
                elif sign == ']' and before_sign == '[':
                    pass
                elif sign == '}' and before_sign == '{':
                    pass
                else:
                    return False
        if stack:
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid(''))
    print(solution.isValid('()]'))
    print(solution.isValid('()'))
    print(solution.isValid('()[]{}'))
    print(solution.isValid('(]'))
    print(solution.isValid('([)]'))
    print(solution.isValid('{[]}'))
