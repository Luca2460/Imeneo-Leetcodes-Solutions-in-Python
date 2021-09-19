# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#     # RECURSIVE
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False
        
#         if root.val == targetSum and not root.left and not root.right: return True
        
#         return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
    
    
    # ITERATIVE WITH STACK - TOP-DOWN
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, targetSum)]
        
        while stack:
            curr, target = stack.pop()
            
            if not curr.left and not curr.right and target == curr.val: return True
            
            if curr.left:
                stack.append((curr.left, target - curr.val))
            if curr.right:
                stack.append((curr.right, target - curr.val))
            
        return False
        # TIME complexity: O(N) in both recursive and iterative implementation, as we might have to check every node in the tree
        # SPACE complexity: O(logN) for a balanced tree, as we only keep one branch/path in memory at the time, 
        # O(N) in worst case where tree is a list.
