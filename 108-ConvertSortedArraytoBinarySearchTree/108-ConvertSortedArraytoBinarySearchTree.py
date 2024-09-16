# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.treeHelper(0, len(nums) - 1, nums)
    
    def treeHelper(self, left, right, nums):
        if left > right:
            return None
        
        mid = (left + right) // 2
        print(f"Left: {left}")
        print(f"Right: {right}")
        print(f"Mid: {mid}")
        root = TreeNode(nums[mid])
        root.left = self.treeHelper(left,  mid - 1, nums)
        root.right = self.treeHelper(mid + 1, right, nums)
        return root
