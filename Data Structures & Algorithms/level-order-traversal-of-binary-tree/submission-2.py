# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Create list to be returned
        res = []
        #Creates a queue
        q = collections.deque()
        #Append root
        q.append(root)
        #Loop while queue has values
        while q:
            #Amount of nodes in the current level
            qLen = len(q)
            level = []
            #Repeat for the # nodes in the level
            for i in range(qLen):
                #Node == oldest element in the queue
                node = q.popleft()
                #If node is not null
                if node:
                    #Append current node val to the level sublist
                    level.append(node.val)
                    #Append its left and right children to the tree
                    q.append(node.left)
                    q.append(node.right)
                #If level is not null we append it to res
            if level:
                res.append(level)
        return res 
        