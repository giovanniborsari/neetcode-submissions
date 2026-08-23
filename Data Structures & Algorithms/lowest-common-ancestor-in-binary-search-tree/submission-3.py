# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #None case
        if not root or not p or not q:
            return None
        
        #Check if both are on the right
        if (min(q.val, p.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q )
        #Check if both are on the left
        elif (max(q.val, p.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q )
        #If both if and elif are false I know I have a split
        else:
            return root

        
        

        
        

    
        
        
             
