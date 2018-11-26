"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true

Note:
You may assume both s and t have the same length.

"""


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        time complexity : O(n)
        """
        if len(s) != len(t):
            return False
        s_ch_map, t_ch_map = {}, {}
        for i, val in enumerate(s):
            s_ch_map[val] = s_ch_map.get(val, []) + [i]
        for i, val in enumerate(t):
            t_ch_map[val] = t_ch_map.get(val, []) + [i]
        return sorted(s_ch_map.values()) == sorted(t_ch_map.values())


if __name__ == '__main__':
    solution = Solution()
    print(solution.isIsomorphic("egg", "add"))
    print(solution.isIsomorphic("foo", "bar"))
    print(solution.isIsomorphic("paper", "title"))
    print(solution.isIsomorphic("abxx", "etta"))
    print(solution.isIsomorphic("aba", "baa"))
    print(solution.isIsomorphic("accaat", "xbbxxa"))
