"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".

"""


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        data = []
        for index in range(len(s)):
            ch = s[index]
            if ch in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                data.append(index)

        for index in range(len(data) // 2):
            temp = s_list[data[index]]
            s_list[data[index]] = s_list[data[len(data) - 1 - index]]
            s_list[data[len(data) - 1 - index]] = temp
        return ''.join(s_list)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseVowels("hello"))
    print(solution.reverseVowels("leetcode"))
