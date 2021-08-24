# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # better recursive solution.
        if not head or not head.next:
            return head
        previous = head
        curr = head.next
        head.next = None
        
        while curr:
            temp = curr.next
            curr.next = previous
            previous = curr
            curr = temp
        
        return previous
        # TIME complexity: O(N)
        # SPACE complexity: O(1)

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


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # RECURSIVE came up with it myself, except for "head.next = None"
        if not head or not head.next: # check if list is empty or if end was reached
            return head
        
        newHead = self.reverseList(head.next) # solve the next of the list before I change head.next
        
        if not head.next.next: # if I am at the last but one node or earlier, make the next node point to me
            head.next.next = head
            head.next = None # set next head to None, otherwise the last node in the recursion (the first in the list) will have its next still pointing towards the second one
            
        return newHead

        # TIME complexity: O(N)
        # SPACE complexity: O(N) (due to the recursive stack)