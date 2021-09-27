# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        
        head = TreeNode(root.val)
        n = head
        
        stack = []
    
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
        
        while stack:
            node = stack.pop()
            n.right = TreeNode(node.val)
            n = n.right
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
                
        root.left = None
        root.right = head.right
        # TIME complexity: O(N), have to visit every node
        # SPACE complexity: O(N), due to the stack and secondary tree created