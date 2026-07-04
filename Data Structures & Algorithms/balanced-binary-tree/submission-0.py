# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def lenbran(root:Optional[TreeNode],lenght:int = 0)->int:
            if root is None :
                return lenght
            return max(lenbran(root.left,lenght+1),lenbran(root.right,lenght+1))
        def check(root:Optional[TreeNode])->bool:
            if root is None:
                return True
            base = bool(abs(lenbran(root.right)-lenbran(root.left))<=1)
            return base and check(root.right) and check(root.left)
        
        return check(root)
        