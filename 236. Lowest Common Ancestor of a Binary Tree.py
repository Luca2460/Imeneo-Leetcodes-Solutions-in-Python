# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lowestCommonAncestorAux(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if not root: return [0,0,0]

            left = lowestCommonAncestorAux(root.left, p, q)
            right = lowestCommonAncestorAux(root.right, p, q)

            if left[2]:
                return [1,1,left[2]]
            if right[2]: 
                return [1,1,right[2]]

            res = [0,0,0] # (p was found, q was found, the lowestCommonAncestor was found)
            if left[0] or right[0] or root == p: res[0] = 1
            if left[1] or right[1] or root == q: res[1] = 1

            if res[0] and res[1]: return [1,1,root]

            return res
        
        return lowestCommonAncestorAux(root,p,q)[2]
        # TIME complexity: O(N)
        # SPACE complexity: O(N) worst case, O(logN) balanced tree. The recursion stack exends for the length of a branch.