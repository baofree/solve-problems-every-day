class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        input_bin = list(bin(n)[2:].zfill(32))
        result = 0
        for index in range(len(input_bin)):
            result += (2 ** index) * int(input_bin[index])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseBits(43261596)) # 00000010100101000001111010011100
