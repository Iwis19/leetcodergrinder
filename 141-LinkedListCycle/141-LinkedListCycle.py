# Last updated: 3/27/2026, 1:35:08 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        """
        1. honestly didnt know that i could add nodes into sets but i have no clue why i thought i couldnt
        2. implemented by myself, will try tortoise and hare method right after

        47 ms beats 89%
        """

        visited_nodes = set()
        ptr = head

        while ptr:
            if ptr in visited_nodes:
                return True
            visited_nodes.add(ptr)

            ptr = ptr.next

        return False
