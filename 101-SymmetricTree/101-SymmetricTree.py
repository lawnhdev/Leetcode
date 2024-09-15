# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
what I tried, it almost works but it doesn't pass this test case where root = [1,2,2,2,null,2] and it is driving me insane:

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        inOrderNodeList = self.inOrderTraversalHelper(root)
        print(inOrderNodeList)
        leftPtr = 0
        rightPtr = len(inOrderNodeList) - 1
        while leftPtr <= rightPtr:
            if inOrderNodeList[leftPtr] != inOrderNodeList[rightPtr]:
                return False
            leftPtr += 1
            rightPtr -= 1
        return True

    def inOrderTraversalHelper(self, root: Optional[TreeNode]):
        ret = []
        if not root:
            return []
        ret += self.inOrderTraversalHelper(root.left)
        ret.append(root.val)
        ret += self.inOrderTraversalHelper(root.right)
        return ret
'''        

''' similar solution to mine that I found (its also not very good) '''
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.inorder(root.left, root.right)
    
    def inorder(self, root1:  Optional[TreeNode], root2: Optional[TreeNode]):
        print(root1)
        print(root2)
        try:
            if root1 or root2:
                if root1.val!=root2.val:
                    return False
                a=self.inorder(root1.left,root2.right)
                b=self.inorder(root1.right,root2.left)
                if a==False or b==False:
                    return False
        except:
            return False
        return True
