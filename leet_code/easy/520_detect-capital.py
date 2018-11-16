"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".

Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:
Input: "USA"
Output: True

Example 2:
Input: "FlaG"
Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

"""


class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool

        Time complexity : O(n)
        """
        if len(word) <= 1:
            return True
        if not word[0].isupper() and word[1].isupper():
            return False
        for index in range(2, len(word)):
            if word[index].isupper() != word[index - 1].isupper():
                return False
        return True

    def detectCapitalUse2(self, word):
        """
        Time complexity : O(n)
        :param word:
        :return:
        """
        if word == '':
            return False
        if word.upper() == word or word.lower() == word:
            return True
        elif word.lower().capitalize() == word:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.detectCapitalUse('USA'))
    print(solution.detectCapitalUse('Flag'))
    print(solution.detectCapitalUse('leetcode'))
    print(solution.detectCapitalUse('Google'))
    print(solution.detectCapitalUse('aSk'))
    print(solution.detectCapitalUse('aS'))
    print(solution.detectCapitalUse('a'))
    print(solution.detectCapitalUse('A'))
