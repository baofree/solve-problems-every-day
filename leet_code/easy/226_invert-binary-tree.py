from leet_code import helper

"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), 
but you can’t invert a binary tree on a whiteboard so f*** off.
"""


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return []
        queue = [root]

        while queue:
            cur = queue.pop(0)
            temp = cur.left
            cur.left = cur.right
            cur.right = temp

            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)

        return root

    def invertTree2(self, root):
        if root is None:
            return
        right = self.invertTree2(root.right)
        left = self.invertTree2(root.left)
        root.left = right
        root.right = left
        return root


if __name__ == '__main__':
    solution = Solution()
    print(solution.invertTree(helper.gen_bin_tree([4, 2, 7, 1, 3, 6, 9])))
    print(solution.invertTree(helper.gen_bin_tree([4, 2, 7, 1, 3, 6])))
    print(solution.invertTree(helper.gen_bin_tree([1, 2])))
    print(solution.invertTree(helper.gen_bin_tree([])))

    # print(solution.invertTree2(helper.gen_bin_tree([4, 2, 7, 1, 3, 6, 9])))
    # print(solution.invertTree2(helper.gen_bin_tree([4, 2, 7, 1, 3, 6])))
    # print(solution.invertTree2(helper.gen_bin_tree([1, 2])))
    # print(solution.invertTree2(helper.gen_bin_tree([])))
