class Solution:
    def rob(self, nums: List[int]) -> int:

        """
        another fib sequence problem

        actually had no idea how to start this dp problem even though i knew this was a fib sequence problem since i found it under neetcode

        with some help, i realized this is a bottom up question, so iteration + N var since i only need to worry about what i have from i-1 houses ago or currenthouse + i-2 houses ago.... so therefore 2 state variables i need to know about consistently

        also wondered why im using for value in nums, and not for i in range(2, len(n)), but that was stupid since it wouldve been a recursive solution if i HAD to do that, which is inefficient AND wrong to do

        0 ms runtime beats 100
        """
       
        previous = most = 0

        for value in nums:
            previous, most = most, max(most, previous + value)

        return most
