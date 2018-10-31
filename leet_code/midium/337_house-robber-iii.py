"""
The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called the "root." Besides the root,
each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this place forms a binary tree".
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
from leet_code import helper


class Solution(object):
    def find_max(self, root):
        if root is None:
            return [0, 0]
        x = self.find_max(root.left)
        y = self.find_max(root.right)
        return [root.val + x[1] + y[1], max(x[0], x[1]) + max(y[0], y[1])]

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.find_max(root))


if __name__ == '__main__':
    solution = Solution()
    # print(solution.rob(helper.gen_bin_tree([3, 2, 3, None, 3, None, 1])))  # 7
    # print(solution.rob(helper.gen_bin_tree([3, 4, 5, 1, 3, None, 1])))  # 9
    print(solution.rob(helper.gen_bin_tree([4, 1, None, 2, None, 3])))  # 7
