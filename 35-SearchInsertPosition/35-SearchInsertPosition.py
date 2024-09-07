'''
my attempt:


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        

        middleIndex = len(nums) // 2
        trackingIndex = middleIndex
        print(trackingIndex)
        while len(nums) > 1:
            middleNum = nums[middleIndex]
            if target == middleNum:
                return trackingIndex
            elif target > middleNum:
                nums = nums[middleIndex:]
                middleIndex = len(nums) // 2
                if middleIndex == 0:
                    trackingIndex += 1
                else:
                    trackingIndex += middleIndex
            else:
                nums = nums[:middleIndex]
                middleIndex = len(nums) // 2
                if middleIndex == 0:
                    trackingIndex -= 1
                else:
                    trackingIndex -= middleIndex
            print(nums)
            print(trackingIndex)
        
        if trackingIndex == 0:
            if target > nums[0]:
                return 1
            else:
                return 0
        elif trackingIndex == 1:
            if target > nums[0]:
                return trackingIndex
            else:
                return 0
        else:
            if target > nums[0]:
                return trackingIndex + 1
            else:
                return trackingIndex - 1
        if trackingIndex == 0:
            if target > nums[0]:
                return 1
            else:
                return 0
        else:
            return trackingIndex
    '''

# solution
class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l