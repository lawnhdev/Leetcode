# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    '''
    close but no dice 


    pathSumExists = False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        hasLeftPath = False
        hasRightPath = False
        if root:
            if root.left:
                leftPath = self.treeHelper(root.left, targetSum)
                leftPath[0] -= root.val
                leftPath[1] -= root.val
                print(f"LeftPath: {leftPath}")
                hasLeftPath = leftPath[0] == 0 or leftPath[1] == 0
            if root.right:
                rightPath = self.treeHelper(root.right, targetSum)
                rightPath[0] -= root.val
                rightPath[1] -= root.val
                print(f"RightPath: {rightPath}")
                hasRightPath = rightPath[0] == 0 or rightPath[1] == 0
            if not root.left and not root.right and root.val == targetSum:
                return True

        return hasLeftPath or hasRightPath

    def treeHelper(self, root: Optional[TreeNode], targetSum: int):
        if not root:
            return None
        else:
            if root.left and not root.right:
                temp = self.treeHelper(root.left, targetSum)
                ret = [temp[0] - root.val, temp[1] - abs(root.val)]
                print(f"Root.val: {root.val}")
                print(f"Left, but not right: {ret}")
            elif not root.left and root.right:
                temp = self.treeHelper(root.right, targetSum)
                ret = [temp[0] - root.val, temp[1] - abs(root.val)]
                print(f"Root.val: {root.val}")
                print(f"Right, but not left: {ret}")
            elif not root.left and not root.right:
                # child node
                ret = [targetSum - root.val, targetSum - root.val]
                print(f"Root.val: {root.val}")
                print(f"Child Node: {ret}")
            else:
                ret = [self.treeHelper(root.left, targetSum)[0] - root.val, self.treeHelper(root.right, targetSum)[1] - root.val]
                print(f"Root.val: {root.val}")
                print(f"Right and Left: {ret}")
            return ret
        '''

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, curSum):
            if not node:
                return False
            
            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum
            
            return (dfs(node.left, curSum) or dfs(node.right, curSum))
        
        return dfs(root, 0)
                
