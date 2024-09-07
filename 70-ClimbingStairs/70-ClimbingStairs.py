class Solution:

    def __init__(self):
        self.memo = {}

    # doing it recursively normally will exceed the time limit, because its O(2^n), but we can use memoization to make it O(n)
    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]


    '''
    n == 2

    1. 1 step + 1 step
    2. 2 steps

    n == 3

    1. 1 step + 1 step + 1 step
    2. 1 step + 2 step
    3. 2 step + 1 step

    n == 4

    1. 1 step + 1 step + 1 step + 1 step
    2. 1 step + 2 step + 1 step
    3. 1 step + 1 step + 2 step
    4. 2 step + 1 step + 1 step
    5. 2 step + 2 step

    n == 5

    1. 1 step + 1 step + 1 step + 1 step + 1 step
    2. 1 step + 2 step + 1 step + 1 step
    3. 1 step + 1 step + 2 step + 1 step
    4. 1 step + 1 step + 1 step + 2 step
    5. 2 step + 1 step + 1 step + 1 step
    6. 2 step + 1 step + 2 step
    7. 2 step + 2 step + 1 step

    '''


        
