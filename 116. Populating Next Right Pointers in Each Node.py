"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# from collections import deque
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if not root: return root
        
#         q = deque()
#         q.append(root)
#         q2 = deque()
        
#         nx = None
        
#         while q:
#             while q:
#                 node = q.pop()
#                 if node.right:
#                     q2.appendleft(node.right)
#                     q2.appendleft(node.left) # we know the tree is perfect, so no need for the second if
                    
#                 node.next = nx
#                 nx = node
#             nx = None
#             q = q2
#             q2 = deque()
        
#         return root
          # TIME complexity: O(N)
          # SPACE complexity: O(N)
    
    # FOLLOW-UP only constant extra space allowed; however, extra space for recursion is fine
class Solution:
    leftmost = None
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        self.leftmost = root
        root.next = None
        
        def aux(self, node):
            if not node.left: return
            
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
                aux(self, node.next)
            else:
                node.right.next = None
                if not self.leftmost.left.left: return
                self.leftmost = self.leftmost.left
                aux(self, self.leftmost)
            
        aux(self, root)
        return root
        # TIME complexity: O(N)
        # SPACE complexity: O(1) excluding recursion. An iterative approach can also be used to do it in O(1)