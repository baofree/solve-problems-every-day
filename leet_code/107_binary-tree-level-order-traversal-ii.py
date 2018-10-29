from leet_code import helper


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = []
        result = []
        queue.append(root)
        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.insert(0, level)
        return result


if __name__ == '__main__':
    solution = Solution()
    tree = helper.gen_bin_tree([3, 9, 20, None, None, 15, 7])
    print(solution.levelOrderBottom(tree))
