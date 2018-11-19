"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:

We should return its max depth, which is 3.


Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.

"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        result = 0
        if root is None:
            return result

        queue = [root]

        while queue:
            level_len = len(queue)

            for i in range(level_len):
                node = queue.pop()
                for node in node.children:
                    queue.insert(0, node)
            result += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxDepth(None))
