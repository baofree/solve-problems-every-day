"""
Given a non-empty array of non-negative integers nums,
the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

"""


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        left_index = {}
        right_index = {}
        for index in range(len(nums)):
            num = nums[index]
            if num not in counts:
                counts[num] = 0
                left_index[num] = index
                right_index[num] = index
            counts[num] += 1
            right_index[num] = index

        max_count = 0
        result = 50001

        for key in counts:
            if max_count < counts[key]:
                max_count = counts[key]
                result = (right_index[key] + 1) - left_index[key]
            elif max_count == counts[key]:
                result = min(result, (right_index[key] + 1) - left_index[key])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findShortestSubArray([1, 2, 2, 3, 1]))
    print(solution.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))
