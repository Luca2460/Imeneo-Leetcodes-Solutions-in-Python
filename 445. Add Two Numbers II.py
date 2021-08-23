# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: # This solution is not really beautiful

        res = 0
        
        curr1 = l1
        curr2 = l2
        len1, len2 = 0, 0
        
        while curr1:
            len1 += 1
            curr1 = curr1.next
            
        while curr2:
            len2 += 1
            curr2 = curr2.next
        

        i = 1
        while l1 or l2:
            if l1:
                res += l1.val * 10 **(len1-i)
                l1 = l1.next
            if l2:
                res += l2.val * 10 **(len2-i)
                l2 = l2.next
            i += 1
        

        resList = ListNode()
        tail = resList
        
        for i in range(len(str(int(res))), 0, -1):
            tail.next = ListNode()
            tail = tail.next
            
            tail.val, res = divmod(res, 10**(i-1))
            tail.val = int(tail.val)
        
        return resList.next

        # TIME complexity: O(max(N+M)), where N and M are the lengths of the 2 input strings
        # SPACE complexity: O(max(N+M)), or O(1) if the output list is not taken into account