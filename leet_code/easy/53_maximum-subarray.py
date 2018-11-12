"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.

"""
import sys


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                result = max(result, sum)
        return result

    def maxSubArray1(self, nums):
        pre = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            pre = max(nums[i], nums[i] + pre)
            result = max(result, pre)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(solution.maxSubArray1([-1]))  # -1
    print(solution.maxSubArray1(
        [-57, 9, -72, -72, -62, 45, -97, 24, -39, 35, -82, -4, -63, 1, -93, 42, 44, 1, -75, -25, -87, -16, 9, -59, 20,
         5, -95, -41, 4, -30, 47, 46, 78, 52, 74, 93, -3, 53, 17, 34, -34, 34, -69, -21, -87, -86, -79, 56, -9, -55,
         -69, 3, 5, 16, 21, -75, -79, 2, -39, 25, 72, 84, -52, 27, 36, 98, 20, -90, 52, -85, 44, 94, 25, 51, -27, 37,
         41, -6, -30, -68, 15, -23, 11, -79, 93, -68, -78, 90, 11, -41, -8, -17, -56]))
