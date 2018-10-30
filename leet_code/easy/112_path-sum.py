"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


"""
from leet_code import helper


class Solution:

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            if root.val == sum:
                return True
            return False
        if self.hasPathSum(root.left, sum - root.val):
            return True

        if self.hasPathSum(root.right, sum - root.val):
            return True

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.hasPathSum(helper.get_bin_tree(), 22))
    pass
