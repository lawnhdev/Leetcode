class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number = 0
        baseMultiplier = 1
        for char in columnTitle[::-1]:  # Reverse the string
            digit = ord(char) - 64
            print(digit)
            number += digit * baseMultiplier
            baseMultiplier *= 26
        return number
        
