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
#                 if node.left:
#                     q2.appendleft(node.left)
                    
#                 node.next = nx
#                 nx = node
#             nx = None
#             q = q2
#             q2 = deque()
        
#         return root
    
    
    # FOLLOW-UP space complexity O(1)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        
        def findNext(parent):
            while parent.next:
                parent = parent.next

                if parent.left:
                    return parent.left

                if parent.right:
                    return parent.right
            return None

        root.next = None
        
        leftmost = root
        new_leftmost = root
        node = root
        
        while new_leftmost:
            while node:
                if node.left:
                    if node.right:
                        node.left.next = node.right
                    else:
                        node.left.next = findNext(node)
                if node.right:
                    node.right.next = findNext(node)
                node = node.next
                
            new_leftmost = None
            while not new_leftmost and leftmost:
                if leftmost.left:
                    new_leftmost = leftmost.left
                elif leftmost.right:
                    new_leftmost = leftmost.right
                leftmost = leftmost.next
                
            leftmost = new_leftmost
            node = leftmost
            
        return root
        # TIME complexity: O(N), we have to traverse every node
        # SPACE complexity: O(1), we don't make use of any additional data structure