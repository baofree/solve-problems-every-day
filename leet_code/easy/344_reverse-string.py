"""
Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"

Example 2:
Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"


"""


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        for index in range(len(s) // 2):
            temp = s[index]
            s[index] = s[len(s) - 1 - index]
            s[len(s) - 1 - index] = temp
        return ''.join(s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseString('hello'))
    print(solution.reverseString('A man, a plan, a canal: Panama'))
