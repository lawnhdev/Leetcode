# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # need to verify that for every node, that the min and max depth for every child node is within 1
        # to understand better see this test case: [1,2,2,3,null,null,3,4,null,null,4]

        if not root:
            return True
        else:
            left = self.findMaxDepthHelper(root.left)
            right = self.findMaxDepthHelper(root.right)
            diff = abs(left - right)
            if diff > 1:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
        

    def findMaxDepthHelper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            print(f"In Max: {root.val}")
            return 1 + max(self.findMaxDepthHelper(root.left), self.findMaxDepthHelper(root.right))

    '''def findMinDepthHelper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            print(f"In Min: {root.val}")
            return 1 + min(self.findMinDepthHelper(root.left), self.findMinDepthHelper(root.right))
    '''
