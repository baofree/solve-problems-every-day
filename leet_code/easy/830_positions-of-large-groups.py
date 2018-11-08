"""
In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.



Example 1:
Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.

Example 2:
Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.

Example 3:
Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]


Note:  1 <= S.length <= 1000


"""


class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """

        result = []

        if len(S) < 3:
            return result

        position = [None, None]

        for index in range(1, len(S)):
            if position[0] is None and S[index] == S[index - 1]:
                position[0] = index - 1
            elif position[0] is not None and S[index] == S[index - 1]:
                position[1] = index
            elif position[0] is not None and S[index] != S[index - 1]:
                if position[1] is not None and position[1] - position[0] >= 2:
                    result.append([position[0], position[1]])
                position = [None, None]
        if (position[0] is not None and position[1] is not None) and position[1] - position[0] >= 2:
            result.append([position[0], position[1]])
        return result

    def largeGroupPositions1(self, S):

        result = []

        index1 = 0

        for j in range(len(S)):
            if j == len(S) - 1 or S[j] != S[j + 1]:
                if j - index1 >= 2:
                    result.append([index1, j])
                index1 = j + 1
        return result


if __name__ == '__main__':
    solution = Solution()
    # print(solution.largeGroupPositions('abbxxxxzzy'))  # [[3,6]]
    # print(solution.largeGroupPositions('abc'))
    # print(solution.largeGroupPositions('abcdddeeeeaabbbcd'))
    # print(solution.largeGroupPositions('aaa'))
    # print(solution.largeGroupPositions('aa'))

    # print(solution.largeGroupPositions1('bababbaba'))
    print(solution.largeGroupPositions1('aaa'))
