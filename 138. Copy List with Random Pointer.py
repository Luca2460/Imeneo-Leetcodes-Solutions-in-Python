
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        newHead = Node(head.val)
        node = newHead
        nOld = head.next
        
        nodesToPositions = {head:0}
        positionsToNewNodes = [newHead]
        
        i = 1
        while nOld:
            node.next = Node(nOld.val)
            nodesToPositions[nOld] = i
            positionsToNewNodes.append(node.next)
            node = node.next
            nOld = nOld.next
            i += 1
        node.next = None
        
        i = 0
        nOld = head
        node = newHead
        while node:
            if not nOld.random:
                node.random = None
            else:
                node.random = positionsToNewNodes[nodesToPositions[nOld.random]]
            nOld = nOld.next
            node = node.next
            i += 1
        
        return newHead
        # TIME complexity: O(N)
        # SPACE complexity: O(N)