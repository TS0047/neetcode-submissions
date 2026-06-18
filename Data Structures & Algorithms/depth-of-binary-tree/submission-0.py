# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_d = 0

    def maxDepth(self, root: Optional[TreeNode], depth=0) -> int:
        if root:
            self.max_d = max(self.max_d,depth+1)
            if root.right:
                self.maxDepth(root.right,depth+1)
            if root.left:
                self.maxDepth(root.left,depth+1)
        return self.max_d        

    
