# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode: # I had to look at the solutions, but only partially
        res = ListNode()
        res_tail = res # dummy head needed to traverse the list
        
        carry = 0
        
        while l1 or l2 or carry: # if l1==null and l2==null and there is no carry, the loop will break
            res_tail.next = ListNode()
            res_tail = res_tail.next    
            
            if l1:
                res_tail.val += l1.val
                l1 = l1.next
                
            if l2:
                res_tail.val += l2.val
                l2 = l2.next
                
            if carry == 1:
                res_tail.val += 1
                carry = 0
            
            if res_tail.val >= 10:
                res_tail.val -= 10
                carry = 1
            

            
        return res.next # skips the node we created in the beginning since it was not used

        # TIME complexity: O(max(M+N)), where M and N are the length of the input numbers-lists
        # SPACE complexity: O(max(M+N)) (which is roughly the length of the result list, excluding the carry)