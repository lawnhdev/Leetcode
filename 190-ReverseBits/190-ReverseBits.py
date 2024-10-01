class Solution:
    def reverseBits(self, n: int) -> int:
        reversedBitString = ""
        while n > 0:
            digit = n % 2
            reversedBitString += str(digit)
            n //= 2
        print(reversedBitString)
        print(len(reversedBitString))
        # we have to return a string that has 32 bits, so if our string is less than length 32 then we must fill it with zeroes at the back until it is 32 bits
        # Create a string of zeros
        zero_string = '0' * (32 - len(reversedBitString))
        reversedBitString += zero_string
        print(reversedBitString)
        return int(reversedBitString, 2)
