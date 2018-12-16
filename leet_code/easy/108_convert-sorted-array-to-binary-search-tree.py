"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem,
a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""
from leet_code import helper


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def convert(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = helper.TreeNode(nums[mid])
            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)
            return node

        return convert(0, len(nums) - 1)

    def print(self, root):
        if not root:
            return
        self.print(root.left)
        print(root.val)
        self.print(root.right)


if __name__ == '__main__':
    solution = Solution()
    result = solution.sortedArrayToBST([-10, -3, 0, 5, 9])
    solution.print(result)
