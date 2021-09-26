# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        printed = []
        def inOrder(root):
            if not root: return True
            
            left = inOrder(root.left)
            if printed: 
                if root.val <= printed[-1]: return False
                printed.pop()
            printed.append(root.val)
            right = inOrder(root.right)
            return left and right
        
        return inOrder(root)
        # TIME complexity: O(N) has to visit every node
        # SPACE complexity: O(N) due to recursion stack