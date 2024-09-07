class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        newlist = []
        for i in range(len(nums)):
            if nums[i] != val:
                newlist.append(nums[i])
        print(newlist)
        nums[:] = newlist # updates the original list in place
        print(nums)
        return len(nums)
        