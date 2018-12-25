"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:
Input:
["a","a","b","b","c","c","c"]
Output:
Return 6, and the first 6 characters of the input array should be:
["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

"""


class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        read = write = 0
        char_len = len(chars)
        while read < char_len:
            ch = chars[read]
            count = 0
            while read < char_len and chars[read] == ch:
                read += 1
                count += 1
            chars[write] = ch
            write += 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        return write


if __name__ == '__main__':
    solution = Solution()
    print(solution.compress(["a", "a", "b", "b", "c", "c", "c"]))
    print(solution.compress(["a", "b", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"]))
    # print(solution.compress(["a", "a", "b", "b", "c", "c", "c", "d"]))
    # print(solution.compress(["aa", "aa", "b", "b", "c", "c", "c", "d"]))
