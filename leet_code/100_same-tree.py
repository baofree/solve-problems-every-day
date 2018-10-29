"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is not None and q is not None:
            if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
        return False


from leet_code import helper

if __name__ == '__main__':
    """
    [10,5,15]
    [10,5,null,null,15]
    """
    solution = Solution()
    p = helper.TreeNode(1)
    p.left = helper.TreeNode(2)
    p.right = helper.TreeNode(3)
    # p.left.left = helper.TreeNode(4)

    q = helper.TreeNode(1)
    q.left = helper.TreeNode(2)
    q.right = helper.TreeNode(3)

    print(solution.isSameTree(p, q))
