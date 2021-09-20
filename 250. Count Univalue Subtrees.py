# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int: # came up with it myself. Is not super fast tho, it takes twice the time it should.
        return self.countUnival(root)[0]
        
    def countUnival(self, root):
        if not root: return (0 , 0) # flag == 1 => the univalue tree was interrupted
        
        left_count, left_flag = self.countUnival(root.left)
        right_count, right_flag = self.countUnival(root.right)
        
        if left_flag or right_flag: return (left_count + right_count, 1)
        
        if root.left:
            if root.left.val != root.val: return (left_count + right_count, 1)
        if root.right:
            if root.right.val != root.val: return (left_count + right_count, 1)
        
        return (right_count + left_count + 1, 0)
        # TIME complexity: O(N) has to visit all the nodes of the tree, and does so exactly once
        # SPACE complexity: O(logN) for a balanced tree, O(N) worst case where tree degenerates into a list