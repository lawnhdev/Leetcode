class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ret = ""
        while columnNumber > 0:
            print(columnNumber)
            if columnNumber > 26 and columnNumber % 26 != 0:
                digit = columnNumber % 26
                print(digit + 64)
                ret += chr(digit + 64)
            elif columnNumber > 26 and columnNumber % 26 == 0:
                ret += chr(90) # weird case with multiples of 26 like 52
                columnNumber -= 26
            else:
                digit = columnNumber
                print(digit + 64)
                ret += chr(digit + 64)
                break;
            columnNumber //= 26
        return ret[::-1] # reverse the string
