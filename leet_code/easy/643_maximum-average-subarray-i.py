"""
Given an array consisting of n integers,
find the contiguous subarray of given length k that has the maximum average value.
And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].


"""


class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sums = [0]
        for x in nums:
            sums.append(sums[-1] + x)
        max_val = max(sums[i + k] - sums[i]
                      for i in range(len(nums) - k + 1))
        return max_val / k


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
    print(solution.findMaxAverage([0, 4, 0, 3, 2], 1))  # 4.0
