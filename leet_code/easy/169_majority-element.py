"""
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
"""


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_map = {}

        for num in nums:
            if num not in count_map:
                count_map[num] = 0
            count_map[num] += 1
            if count_map[num] > len(nums) / 2:
                return num


if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement([3, 2, 3]))
    print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
