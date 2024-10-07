import time

class Solution:
    def isHappy(self, n: int) -> bool:
        start_time = time.time()
        timeout = 1  # seconds
        summed = n
        my_set = set()
        while summed != 1:
            temp = summed
            if temp in my_set:
                return False
            else:
                my_set.add(temp)
            summed = 0
            while temp > 0:
                digit = temp % 10
                summed += pow(digit, 2)
                temp //= 10
        return True
        
