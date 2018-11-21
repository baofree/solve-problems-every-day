"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6

Example 2:
Input: [1,2,3,4]
Output: 24

Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""
from functools import reduce


class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        time complexity : O(nLog(n))
        """
        nums.sort()
        return max(reduce(lambda a, b: a * b, nums[-3:]), reduce(lambda a, b: a * b, nums[:2] + nums[-1:]))

    def maximumProduct2(self, nums):
        """
        time complexity : O(n)
        """
        max1, max2, max3 = -1001, -1001, -1001
        min1, min2 = 1001, 1001
        for num in nums:
            if num <= min1:
                min2 = min1
                min1 = num
            elif num <= min2:
                min2 = num
            if num >= max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num >= max2:
                max3 = max2
                max2 = num
            elif num >= max3:
                max3 = num
        return max(min1 * min2 * max1, max1 * max2 * max3)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumProduct([1, 2, 3]))
    print(solution.maximumProduct([1, 2, 3, 4]))
    print(solution.maximumProduct([4, 3, 2, 1]))
    print(solution.maximumProduct([-4, -3, -2, -1, 60]))  # 720
    print(solution.maximumProduct2([-4, -3, -2, -1, 60]))  # 720
    print(solution.maximumProduct2([6, 2, 6, 5, 1, 2]))  # 180
    print(solution.maximumProduct([6, 2, 6, 5, 1, 2]))  # 180
