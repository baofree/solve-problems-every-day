"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

"""
from leet_code import helper


class Solution:
    def equals(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        return s.val == t.val and self.equals(s.left, t.left) and self.equals(s.right, t.right)

    def check(self, s, t):
        return s is not None and (self.equals(s, t) or self.check(s.left, t) or self.check(s.right, t))

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.check(s, t)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isSubtree(helper.gen_bin_tree([3, 4, 5, 1, 2]), helper.gen_bin_tree([4, 1, 2])))
    print(solution.isSubtree(helper.gen_bin_tree([3, 4, 5, 1, 2, None, None, None, None, 0]),
                             helper.gen_bin_tree([4, 1, 2])))
