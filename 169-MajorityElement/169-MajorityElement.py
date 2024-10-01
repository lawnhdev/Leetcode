class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countsMap = {}
        for num in nums:
            if num not in countsMap:
                countsMap[num] = 1
            else:
                countsMap[num] += 1
        print(countsMap)
        # Find the key with the highest value
        return max(countsMap, key=countsMap.get)
