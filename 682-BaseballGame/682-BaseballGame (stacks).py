class Solution:
    def calPoints(self, operations: List[str]) -> int:

        """
        1. need to be more flexible on using data structures, i know i used arr like a stack here but i didnt think about stack explicitly on my own.
        2. also chose to convert operation to int first but i couldve just left it to the end, meaning i didnt have to eliminate the possibility of it being a sign/char

        0 ms runtime beats 100
        """

        stack = []

        for operation in operations:

            if operation == '+':
                stack.append(stack[-1] + stack[-2])
            elif operation == "D":
                stack.append(2*stack[-1])
            elif operation == "C":
                stack.pop(-1)
            else:
                stack.append(int(operation))

        return sum(stack)

        
        
