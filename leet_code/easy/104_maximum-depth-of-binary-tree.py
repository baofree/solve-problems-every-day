"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
from leet_code import helper


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = [root]
        level = 0
        while queue:
            level += 1
            level_len = len(queue)
            for index in range(level_len):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return level


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxDepth(helper.gen_bin_tree([3, 9, 20, None, None, 15, 7])))
