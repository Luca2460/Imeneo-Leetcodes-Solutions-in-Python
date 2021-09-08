# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ITERATIVE #
        out = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                out.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            
        return out
        
        # RECURSIVE #
#         if root:
#             res = [root.val]
#             left = self.preorderTraversal(root.left)
#             if left:
#                 res.extend(left)
#             right = self.preorderTraversal(root.right)
#             if right:
#                 res.extend(right)

#             return res
            
            # TIME complexity: O(N)
            # SPACE complexity: O(N) (worst case), O(logN) (average)