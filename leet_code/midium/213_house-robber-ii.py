"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

"""


class Solution(object):
    def find(self, nums):
        even_sum = 0
        odd_sum = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                even_sum = max(even_sum + nums[i], odd_sum)
            else:
                odd_sum = max(odd_sum + nums[i], even_sum)

        return max(even_sum, odd_sum)

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.find(nums[:-1]), self.find(nums[1:]))


if __name__ == '__main__':
    solution = Solution()
    print(solution.rob([2]))  # 2
    print(solution.rob([2, 3, 2]))  # 3
    print(solution.rob([1, 2, 3, 1]))
    print(solution.rob([2, 7, 9, 3, 1]))
    print(solution.rob([2, 1, 1, 2]))  # 4
