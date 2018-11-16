"""
Given an array nums, write a function to move all 0's
to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        last_non_zero = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[last_non_zero] = nums[index]
                last_non_zero += 1
        for index in range(last_non_zero, len(nums)):
            nums[index] = 0
        return nums

    def moveZeroes2(self, nums):
        last_non_zero = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                temp = nums[index]
                nums[index] = nums[last_non_zero]
                nums[last_non_zero] = temp
                last_non_zero += 1
        return nums


if __name__ == '__main__':
    solution = Solution()
    print(solution.moveZeroes([0, 1, 0, 3, 12]))
    print(solution.moveZeroes([0, 0, 1]))
    print(solution.moveZeroes([4, 2, 1]))
    print(solution.moveZeroes([0]))

    print(solution.moveZeroes2([0, 1, 0, 3, 12]))
    print(solution.moveZeroes2([0, 0, 1]))
    print(solution.moveZeroes2([4, 2, 1]))
    print(solution.moveZeroes2([0]))
