class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x <= 2:
            return 1
        for i in range(0, x):
            exp = i * i
            if exp == x:
                return i
            if exp > x:
                return i - 1
        return x
        
