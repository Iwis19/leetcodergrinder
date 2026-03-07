# Last updated: 3/6/2026, 9:31:35 PM
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode(-1)
        self.tail = self.dummy

    def get(self, index:int) -> int:
        i = 0
        current = self.dummy.next # MUST START FROM FIRST REAL NODE
        while current:
            if i == index:
                return current.val
            i+=1
            current = current.next
        return -1
    
    def addAtHead(self, val:int) -> None:
        new_node = ListNode(val)
        
        new_node.next = self.dummy.next
        self.dummy.next = new_node

        if self.dummy == self.tail:
            self.tail = new_node

    def addAtTail(self, val:int) -> None:
        new_node = ListNode(val)
        
        self.tail.next = new_node
        self.tail = self.tail.next

    def addAtIndex(self, index:int, val:int) -> None:
        i = 0
        current = self.dummy
        new_node = ListNode(val)
        while current:
            if i == index:   # so that im on the leftside of where im gonna add
                new_node.next = current.next
                current.next = new_node

                if not new_node.next:
                    self.tail = new_node
                return
            i+=1
            current = current.next
        return -1

    def deleteAtIndex(self, index:int) -> None:
        i = 0
        current = self.dummy
        while current and current.next:
            if i == index:  # 1 node before what im gonna delete
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                return
            i+=1
            current = current.next
        
        
