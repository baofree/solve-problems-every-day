from leet_code import helper

"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""


class Solution:
    def max_depth(self, root):
        if root is None:
            return 0
        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)
        if left_depth is None or right_depth is None:
            return None
        if abs(left_depth - right_depth) > 1:
            return None
        return max(left_depth, right_depth) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.max_depth(root) is not None


if __name__ == '__main__':
    solution = Solution()
    print(solution.isBalanced(helper.gen_bin_tree([3, 9, 20, None, None, 15, 7])))
    print(solution.isBalanced(helper.gen_bin_tree([1, 2, 2, 3, 3, None, None, 4, 4])))
    print(solution.isBalanced(helper.gen_bin_tree([1, 2, 2, 3, None, None, 3, 4, None, None, 4])))  # false
