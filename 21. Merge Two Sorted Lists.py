# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1
        
        if l2.val < l1.val:
            curr1 = l2
            curr2 = l1
        else:
            curr1 = l1
            curr2 = l2
        runner2 = curr2
        head = curr1
        
        while curr1.next:
            while curr1.next and curr1.next.val <= curr2.val:
                curr1 = curr1.next
            if not curr1.next: break
                
            runner2 = curr2
            while runner2.next and runner2.next.val <= curr1.next.val:
                runner2 = runner2.next
            temp = curr1.next
            curr1.next = curr2
            temp2 = runner2.next
            runner2.next = temp
            curr1 = temp
            if not temp2: 
                return head
            curr2 = temp2
            
        if not curr1.next:
            curr1.next = curr2
            
        return head
        # TIME complexity: O(N+M) where N and M are the number of nodes of the two lists respectively
        # SPACE complexity: O(1)