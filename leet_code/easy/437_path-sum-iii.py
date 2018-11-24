"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

"""
from leet_code import helper


class Solution:
    def help(self, root, rest):
        if root is None:
            return 0
        print(root.val)
        cur = int(rest == root.val)
        cur += self.help(root.left, rest - root.val)
        cur += self.help(root.right, rest - root.val)
        return cur

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        # return self.help(root, sum)
        return self.help(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)


if __name__ == '__main__':
    solution = Solution()
    print(solution.pathSum(helper.gen_bin_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8))
