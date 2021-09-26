# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head
        
        if left == right:
            return head

        n = None
        left_node = head
        
        for i in range(left-1):
            n = left_node
            left_node = left_node.next
        
        # n = head
        
        # for i in range(left-2):
        #     n = n.next
            
        # if left == 1: # have to return right node rather than head
        #     left_node = head
        # else:
        #     left_node = n.next
           
        curr = left_node.next
        old = left_node
        
        for i in range(right-left):
            nx = curr.next
            curr.next = old
            old = curr
            curr = nx
            
        left_node.next = curr
        
        if left == 1 : return old
        
        n.next = old
        return head
        # TIME complexity: O(N), one pass
        # SPACE complexity: O(1)