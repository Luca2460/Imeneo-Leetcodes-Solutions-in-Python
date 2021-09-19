# NOT EXECUTABLE (IT REQUIRES AN ACTUAL TREE, IT DOES RUN ON LEETCODE THOUGH)

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: # came up with it myself
        if root == None: return []
        
        q = deque()
        q_aux = deque()
        
        q.append(root)
        
        res = []
        
        k = 0
        while(q):
            res.append([])
            for node in q:
                if node.left:
                    q_aux.append(node.left)
                if node.right:
                    q_aux.append(node.right)    
                res[k].append(node.val)
            k += 1
            q = q_aux
            q_aux = deque()
            
        
        return res
        # TIME complexity: O(N), each node in the tree gets processed exactly once
        # SPACE complexity: O(N), in the worst case, all the nodes are on the same level.
