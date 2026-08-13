# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        """
        yay, mostly did it myself but i got lost in my own sauce with the if statements to check if it wass even or odd and then go on the appropriate node to set the final node.next = None

        but i realized i had n i could just loop to last

        also had a brain fart and forgot to set the curr again after each loop

        3 ms runtime beats 50%, optimal tc but used extra space complexity...

        rule of thumb for modifying linkedlists, always just keep a copy of the curr.next so that you can freely edit curr.next
        """
        
        all_nodes = []

        last = curr = ptr = head

        while ptr:
            all_nodes.append(ptr)
            ptr = ptr.next

        n = len(all_nodes)

        """
        splice logic: 
        1. if even nodes (4) -> 1, 4, 2, 3
        2. if odd nodes (5) -> 1, 5, 2, 4, 3  

        for odd cases, just store the smaller amt in end since the last number wont be touched anyways, will just move and then set next to none for the last node
        """

        end = all_nodes[n//2:]

        print( [node.val for node in end] )

        while end:
            original_next = curr.next
            nxt = end.pop()
            curr.next = nxt
            curr = nxt.next = original_next

        for i in range(n-1):
            last = last.next

        last.next = None
        
        return head
        
