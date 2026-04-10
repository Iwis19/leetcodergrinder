# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        """
        two pointer approach ("fast and slow"?)

        i dont really like how this approach is named, i just feel like one gets a headstart rather than moving faster because theres a linkedlist cycle question that allows me to go fast and slow (2 nodes and 1 node), this is more like gap pointer 

        0 ms runtime beats 100
        """
        
        ptr, temp = head, head

        #move to nth node
        for _ in range(n):
            ptr = ptr.next

        if not ptr:
            return head.next

        #idea is that i keep a constant gap of n nodes between, so when ptr hits the end, temp hits nth node before the end
        #reason why this is ptr.next and not just ptr is because ineed to land right BEFORE when i delete, not right on
        while ptr.next:
            ptr = ptr.next
            temp = temp.next

        temp.next = temp.next.next
        return head
