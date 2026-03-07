# Last updated: 3/6/2026, 9:31:40 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        n1 = l1
        n2 = l2
        output = dummy
        carry_over = 0

        while n1 or n2 or carry_over:
            
            v1 = 0
            if n1:    
                v1 = n1.val

            v2 = 0
            if n2:    
                v2 = n2.val

            sum = v1 + v2 + carry_over

            add = sum % 10
            carry_over = sum // 10

            output.next = ListNode(add)
            output = output.next
            
            if n1:
                n1 = n1.next
            if n2:
                n2 = n2.next
        
        return dummy.next
        