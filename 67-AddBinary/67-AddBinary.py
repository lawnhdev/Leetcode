class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = int(a, 2) + int(b, 2)
        binSum = bin(sum) # this will return a binary string, but it will be prefixed with '0b', i.e: '0b100', so we have to remove the prefix
        return binSum[2:]
