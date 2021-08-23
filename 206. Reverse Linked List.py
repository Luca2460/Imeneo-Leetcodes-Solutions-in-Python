# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # I came up with it myself. It is rather fast but memory intensive
        vals = {}
        
        curr = head
        
        i = 0
        while curr:
            vals[i] = curr.val
            curr = curr.next
            i += 1
            
        curr = head
        while curr:
            curr.val = vals[i-1]
            i = i - 1
            curr = curr.next
            
        return head

        # TIME complexity: O(N), we do 2 passes of the list
        # SPACE complexity: O(N), as we save the whole list in an hashtable buffer