class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower() # have to reassign back to s because these functions return new strings and don't modify the original string because strings are immutable in python
        cleaned = ''.join(char for char in s if char.isalnum()) # only copy alphanumeric characters (letters and numbers)
        print(cleaned)
        
        leftPtr = 0
        rightPtr = len(cleaned) - 1
        
        while leftPtr < rightPtr:
            if cleaned[leftPtr] != cleaned[rightPtr]:
                return False
            leftPtr += 1
            rightPtr -= 1
        return True
