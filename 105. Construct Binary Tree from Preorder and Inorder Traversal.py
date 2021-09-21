# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    preorder_idx = 0
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderHash = {inorder[i]:i for i in range(len(inorder))}
        
        def aux(self, left, right):
            if left > right: return None
            
            val = preorder[self.preorder_idx]
            self.preorder_idx += 1
            
            node = TreeNode(val)
            idx = inorderHash[val]
            
            node.left = aux(self, left, idx - 1)
            node.right = aux(self, idx + 1, right)
            
            return node
        
        return aux(self, 0, len(preorder) - 1)

        # TIME complexity: O(N)
        # SPACE complexity: O(N) due to the hashmap; for the tree: O(N) worst case (only keeps in memory one branch of the tree at the time), O(logN) balanced