# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            ret = [root.val]
            if root.left:
                ret += self.preorderTraversal(root.left)
            if root.right:
                ret += self.preorderTraversal(root.right)
            return ret
        return None
