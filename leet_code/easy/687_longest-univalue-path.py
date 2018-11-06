"""
Given a binary tree, find the length of the longest path where each node in the path has the same value.
This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:
Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:
2

Example 2:
Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:
2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

"""
from leet_code import helper


class Solution(object):
    result = 0

    def longest(self, root):
        if not root:
            return 0
        left_path, right_path = self.longest(root.left), self.longest(root.right)
        left = (left_path + 1) if root.left and root.val == root.left.val else 0
        right = (right_path + 1) if root.right and root.val == root.right.val else 0
        self.result = max(self.result, left + right)
        return max(left, right)

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.longest(root)
        return self.result


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestUnivaluePath(helper.gen_bin_tree([5, 4, 5, 1, 1, None, 5])))
    print(solution.longestUnivaluePath(helper.gen_bin_tree([1, 4, 5, 4, 4, None, 5])))
    print(solution.longestUnivaluePath(helper.gen_bin_tree([5, 5, 5, 5, 5])))
