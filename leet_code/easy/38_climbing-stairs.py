"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.


Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        return self.helper(0, n)

    def helper(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        return self.helper(i + 1, n) + self.helper(i + 2, n)


class Solution1:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [False] * (n + 1)
        return self.helper(0, n, memo)

    def helper(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i]:
            return memo[i]
        memo[i] = self.helper(i + 1, n, memo) + self.helper(i + 2, n, memo)
        return memo[i]


class Solution2:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dp = [False] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


if __name__ == '__main__':
    solution = Solution2()
    print(solution.climbStairs(2))
    print(solution.climbStairs(3))
    print(solution.climbStairs(10))
