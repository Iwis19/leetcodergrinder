class MinStack:

    """
    1. main challenge of this problem is the getMin. i struggled with this.

    i was wondering how to do this in O(1) time, but:
    - create a separate stack that stores mins, the reason why its a stack is that i must be able to pop it easily, but a sorted arr would require me to traverse and pop
    - i was worried that i would pop a number but the way its stored right now it wouldnt be stored in minstack as well
    
    example:
    - stack = [5, 3, 4, 2]
    - min_stack = [5, 3, 2]

    i forgot about stacks properties. reason that it works is that afteri pop 2, ihave:
    - stack = [5,3,4]
    - min_stack = [5,3]

    and i was wondering what if 4 was the min and nothing is done, but the thing is that there is nothing smaller than 3 after it. so therefore, the min element does not change at all. 

    in the same way, thats how im adding min vals to the min_stack. if its not smaller, im nto adding it.

    hope i understand this when i read back.

    0-4 ms runtime beats 100%
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop(-1)
        if self.min_stack and popped == self.min_stack[-1]:
            self.min_stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
