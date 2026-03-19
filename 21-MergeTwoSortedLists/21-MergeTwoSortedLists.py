# Last updated: 3/19/2026, 3:46:03 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        new_list = ListNode(-1)
        curr = new_list

        while list1 or list2:

            if list1:
                val1 = list1.val
            else:
                val1 = 101

            if list2:
                val2 = list2.val
            else:
                val2 = 101

            if val1 >= val2:
                curr.next = ListNode(val2)
                curr = curr.next
                list2 = list2.next

            else:
                curr.next = ListNode(val1)
                curr = curr.next
                list1 = list1.next 

        return new_list.next
        