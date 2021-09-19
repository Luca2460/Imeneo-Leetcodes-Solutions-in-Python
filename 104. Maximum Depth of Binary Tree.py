# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Came up with all the solutions myself

     # ITERATIVE BFS
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        q = deque()
        q_aux = deque()
        q.append(root)
        
        
        depth = 0
        while q:
            for node in q:
                if node.left:
                    q_aux.append(node.left)
                if node.right:
                    q_aux.append(node.right)
            depth += 1
            
            q = q_aux
            q_aux = deque()
        
        return depth
        # TIME complexity: O(N), needs to visit every node
        # SPACE complexity: O(N) average, O(1) best case (if tree is actually a list)


#      # RECURSIVE TOP-DOWN
# class Solution:
#     depth = 0
    
#     def maxDepth(self, root: Optional[TreeNode]) -> int:    
#         self.maxDepthAux(root, 0)
#         return self.depth
        
#     def maxDepthAux(self, root: Optional[TreeNode], prev_depth):  # python does not support overloading 
#         if not root: return
#         if prev_depth +1 > self.depth: self.depth = prev_depth +1 # prev_depth + 1 = curr_depth
#         self.maxDepthAux(root.left, prev_depth+1)
#         self.maxDepthAux(root.right, prev_depth+1)

#         # TIME complexity: O(N)
#         # SPACE complexity: O(N) worst case (tree is actually a list), O(logN) if balanced. It only keeps 1 branch of the tree in memory at the time

    

#     # ITERATIVE TOP-DOWN DFS (memorization: I have a parameter on the top that I use to check while I go down)
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:       
#         if not root: return 0
        
#         stack = [(root,1)]
#         max_depth = 1
        
#         while stack:
#             curr_node, depth = stack.pop()
            
#             if max_depth < depth: max_depth = depth
            
#             if curr_node.left:
#                 stack.append((curr_node.left, depth+1))
            
#             if curr_node.right:
#                 stack.append((curr_node.right, depth+1))
        
#         return max_depth
          # COMPLEXITIES: same as recursive top-down, takes a little less memory cause it uses a stack (does not call the function itself)
    
    
#    # RECURSIVE BOTTOM-UP (memorization: it hits the bottom then returns back up)
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root: return 0
        
#         left_depth = self.maxDepth(root.left)
#         right_depth = self.maxDepth(root.right)
        
#         return max(left_depth, right_depth) + 1
          # COMPLEXITIES: same as recursive top-down, has to visit all nodes and only keeps in memory one branch at the time.