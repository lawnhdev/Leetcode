class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(m, m + n):
            nums1[i] = nums2[m + n - i - 1]
        nums1.sort()
