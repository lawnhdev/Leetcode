# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            if root.left and not root.right:
                return 1 + self.minDepth(root.left)
            elif not root.left and root.right:
                return 1 + self.minDepth(root.right)
            elif root.left and root.right:
                return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
            else:
                return 1
