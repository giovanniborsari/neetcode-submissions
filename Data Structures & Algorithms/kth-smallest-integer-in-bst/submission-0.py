# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = []
        return self.inOrder(root, array)[k-1]

    def inOrder(self,root,array):
        if root:
            #left child
            self.inOrder(root.left,array)

            #visit node
            array.append(root.val)

            #right node
            self.inOrder(root.right,array)
        
        return array
        

        