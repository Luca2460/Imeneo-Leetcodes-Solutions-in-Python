# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]: # did not come up with it myself
        inord = {inorder[i]:i for i in range(len(inorder))}
        
        def buildTreeAux(left, right):
            if left > right: return None

            val = postorder.pop()
            node = TreeNode(val)

            idx = inord[val]
            
            node.right = buildTreeAux(idx +1, right)
            node.left = buildTreeAux(left, idx -1)
            
            return node

                
        return buildTreeAux(0, len(postorder) - 1)
        
        # TIME complexity: O(N) the auxiliary function always returns a node and each node is created through it
        # SPACE complexity: O(N) due to the hashmap and the solution