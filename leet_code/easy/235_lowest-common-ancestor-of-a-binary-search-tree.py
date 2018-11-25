"""
Given a binary search tree (BST),
find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node
in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself
             according to the LCA definition.

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.

"""

from leet_code import helper


class Solution:
    def find(self, root, path, v):
        if root is None:
            return False
        path.append(root)
        if root.val == v:
            return True
        elif root.val < v:
            return self.find(root.right, path, v)
        else:
            return self.find(root.left, path, v)

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_path = []
        self.find(root, p_path, p)
        q_path = []
        self.find(root, q_path, q)

        result = None

        for path in zip(p_path, q_path):
            if path[0] == path[1]:
                result = path[0].val
            else:
                break
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.lowestCommonAncestor(helper.gen_bin_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), 2, 8))
    print(solution.lowestCommonAncestor(helper.gen_bin_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), 2, 4))
