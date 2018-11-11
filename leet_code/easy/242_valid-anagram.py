"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        data_map = {}

        for char in list(s):
            if char not in data_map:
                data_map[char] = 0
            data_map[char] += 1

        for char in list(t):
            if char not in data_map:
                return False
            data_map[char] -= 1
            if data_map[char] == 0:
                data_map.pop(char, None)
        if data_map:
            return False
        return True


if __name__ == '__main__':
    solution = Solution()

    print(solution.isAnagram("anagram", "nagaram"))
    print(solution.isAnagram("rat", "car"))
