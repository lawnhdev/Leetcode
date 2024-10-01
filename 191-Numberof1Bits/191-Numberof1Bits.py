class Solution:
    def hammingWeight(self, n: int) -> int:
        binStr = bin(n)[2:]
        print(binStr)
        return binStr.count('1')
