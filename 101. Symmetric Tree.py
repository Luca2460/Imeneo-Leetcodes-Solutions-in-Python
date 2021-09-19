# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    # BFS sort of. We add the children in such a way that we expect two subsequent elements of the queue to be equal
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool: # my version was more complicated, this is the one from the solutions, traslated into Python
        if not root: return True
        
        q = deque()
        
        q.append(root)
        q.append(root)
        
        while q:
            node1 = q.popleft()
            node2 = q.popleft()
            
            if not node1 or not node2:
                if node1 or node2: return False
            else:
                if node1.val != node2.val: return False
                q.append(node1.left)
                q.append(node2.right)
                q.append(node1.right)
                q.append(node2.left)
        return True
        # TIME complexity: O(N), we need to traverse every node
        # SPACE complexity: O(N) for a balanced tree, O(1) best case
            
                
                

#     # TOP-DOWN recursive. It's top-down cause you first check whether you gotta return error (false), and then you recurse. Bottom-up would recurse first and then do something based on the results of the recursion
# class Solution:
#     def isSymmetric(self, rootLeft: Optional[TreeNode], rootRight="Default") -> bool: # came up with it myself
#         if rootRight == "Default":
#             if not rootLeft: return True
#             return self.isSymmetric(rootLeft.left, rootLeft.right)
        
#         if not rootLeft and not rootRight: return True # base case 1
#         if not rootLeft or not rootRight: return False # base case 2
        
#         if rootLeft.val != rootRight.val: return False
        
#         return self.isSymmetric(rootLeft.left, rootRight.right) and self.isSymmetric(rootLeft.right, rootRight.left)
 
#      # Same top-down but with the usual auxiliary function rather than that ugly default thing
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         return self.isSymmetricAux(root, root)
    
#     def isSymmetricAux(self, rootLeft: Optional[TreeNode], rootRight) -> bool:
#         if not rootLeft and not rootRight: return True # base case 1
#         if not rootLeft or not rootRight: return False # base case 2
        
#         if rootLeft.val != rootRight.val: return False
        
#         return self.isSymmetricAux(rootLeft.left, rootRight.right) and self.isSymmetricAux(rootLeft.right, rootRight.left)