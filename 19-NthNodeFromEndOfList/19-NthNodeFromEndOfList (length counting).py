# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        """
        FROM WEEKS AGO:
        since i want to do it in one pass, i have to make the linked change at n-1th node (1-index based)
        ptr.next = ptr.next.next
        however, for cases where: 
        1st node is removed -> create a dummy node so deletion is easy
        last node is removed
        return head

        1. coded almost evertyhing myself, from idea to finish
        2. however, missed edge case handling like if n is already the length (end) of the linkedlist, then ijust head.next to return an empty linkedlist
        3. came up with deleting length - n + 1, but im not trying to land on the node i delete, its thje one before, so length - n
        4. need to watch out more about indices handling and the order i do it

        note: many other solution used for loops of n to reach the desired node, rather thanw hile, which is indeed a good idea

        0 ms runtime beats 100
        """
        
        length = 0
        ctr = head
        while ctr:
            length += 1
            ctr = ctr.next

        # if what im trying to delete is alr the length of hte linkedlist, then i should just return head.next since assuming its removed
        if n == length:
            return head.next

        ptr = head
        i = 1

        #length 5 linkedlist: 1 2 3 4 5, 2nd node from end, 1 2 3 5, then im removing the 4th node, length - n + 1
        # ADDED COMMENT: but im not trying to land on the node i delete, its thje one before, so length - n

        while ptr.next:
            if i == length - n:
                ptr.next = ptr.next.next
                break
            ptr = ptr.next
            i += 1

        return head

