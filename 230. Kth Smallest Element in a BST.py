# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node = root
        stack = []
        counter = 0
        # Iterative in-order tree traversal
        while True:
            # Go all the way to the left while appending each node you encounter;
            while node:
                stack.append(node)
                node = node.left
            # Once you're at the leaves, process last node;
            node = stack.pop()
            counter += 1
            if counter == k: return node.val
            # After processing, go to the right node and repeat the function from the beginning.
            node = node.right

        # TIME complexity: O(N) worst case, O(logN + k) for balanced tree [note that k is smaller than N anyway]
        # SPACE complexity: O(N) worst case, O(logN) balanced