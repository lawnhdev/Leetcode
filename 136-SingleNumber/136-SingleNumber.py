class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ''' we didnt hit
        l, r = 0, 1

        while r < len(nums) and l != r:
            if nums[l] != nums[r]:
                r += 1
            else:
                if nums[l] == 0 and nums[r] == 0:
                    r += 2
                    l = r - 1
                else:
                    nums[l] = 0
                    nums[r] = 0
                    if r - l == 1: # they are next to each other
                        r += 2
                        l = r - 1
                    else:  
                        l += 1
                        r = l + 1
        if max(nums) != 0:
            return max(nums)
        else:
            return min(nums)

            '''

        # binary xor operator op
        res = 0
        for n in nums:
            res = n ^ res
        return res

                
