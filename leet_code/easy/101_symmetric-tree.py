"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

"""
from leet_code import helper


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.check(root, root)

    def check(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None or tree2 is None:
            return False
        return tree1.val == tree2.val and self.check(tree1.right, tree2.left) and self.check(tree1.left, tree2.right)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isSymmetric(helper.gen_bin_tree([1, 2, 2, 3, 4, 4, 3])))
    print(solution.isSymmetric(helper.gen_bin_tree([1, 2, 2, None, 3, None, 3])))
