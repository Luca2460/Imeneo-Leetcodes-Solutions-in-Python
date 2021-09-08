# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ITERATIVE #
        ans = []
        stack = []
        curr = root
        
        while stack or curr:
            
            if curr:
                stack.append(curr)
                curr=curr.left
            else:
                temp = stack[-1].right
                if not temp:
                    # mean no right child and no left
                    # process the root
                    temp=stack.pop(-1)
                    ans.append(temp.val)
                    while stack and temp == stack[-1].right:
                        # mean this temp node is already right child then now time to process root
                        temp=stack.pop(-1)
                        ans.append(temp.val)
                else:
                    curr=temp
        return ans
            
        
        
        # RECURSIVE #
#         if not root:
#             return
        
#         res = []
        
#         if root.left:
#             res.extend(self.postorderTraversal(root.left))
#         if root.right:
#             res.extend(self.postorderTraversal(root.right))
            
#         res.append(root.val)
        
#         return res