class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        im a dunce, ws doing sliding window wrong

        leftPtr = 0
        rightPtr = len(prices) - 1
        maxProfit = 0
        while leftPtr < len(prices) - 1:
            if leftPtr == rightPtr:
                leftPtr += 1
                rightPtr = len(prices) - 1
                continue
            if prices[leftPtr] > prices[rightPtr]:
                leftPtr += 1
            else:
                currProfit = prices[rightPtr] - prices[leftPtr]
                if currProfit > maxProfit:
                    maxProfit = currProfit
                leftPtr += 1
        return maxProfit
        '''

        l, r = 0, 1 
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r # we found a low price on r so switch l to be r
            r += 1
        return maxP


            

        
