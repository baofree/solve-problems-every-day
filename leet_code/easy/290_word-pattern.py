"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match,
such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

"""


class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern_data = {}
        for index in range(len(pattern)):
            pattern_data[pattern[index]] = pattern_data.get(pattern[index], []) + [index]

        str_data = {}
        str_list = str.split(' ')

        for index in range(len(str_list)):
            str_data[str_list[index]] = str_data.get(str_list[index], []) + [index]

        return sorted(pattern_data.values()) == sorted(str_data.values())


if __name__ == '__main__':
    solution = Solution()
    print(solution.wordPattern("abba", "dog cat cat dog"))
    print(solution.wordPattern("abba", "dog cat cat fish"))
    print(solution.wordPattern("aaaa", "dog cat cat dog"))
    print(solution.wordPattern("abba", "dog dog dog dog"))
