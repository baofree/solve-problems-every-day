"""
The set S originally contains numbers from 1 to n. But unfortunately,
due to the data error, one of the numbers in the set got duplicated to another number in the set,
which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error.
Your task is to firstly find the number occurs twice and then find the number that is missing.
Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.

"""


class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        data_map = {}
        duplicated_num = None
        for index in range(len(nums)):
            if nums[index] not in data_map:
                data_map[nums[index]] = 0
            else:
                duplicated_num = nums[index]
        for num in range(1, len(nums)):
            if num not in data_map:
                return [duplicated_num, num]
        return [duplicated_num, len(nums)]
        # print(len(nums))
        # print(duplicated_num)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findErrorNums([1, 2, 2, 4]))
    print(solution.findErrorNums([1, 1]))
