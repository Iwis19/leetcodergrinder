class Solution:
    def climbStairs(self, n: int) -> int:

            """
            this is essentially fib sequence disguised, as you have can come to n from n-1 AND n-2, and for each n-1 and n-2, theres also n-2, n-3, and n-3, n-4 respectivey...

            a and b start off as f(1), f(2), and f(2) = 2 since theres 2 ways to get to 2

            the loop goes from 3 to n+1 means [3,n]

            no memoization is used here as we dont have that many previous states we need to remember at once

            a,b = b, a+b works better than using a temp since python evaluates right hand side before assigning values. this part is essentialyl just fib(n) = fib(n-1) + fib(n-2), but more efficient since no recursion needed

            0 ms runtime beats 100
            """

            if n <= 2: return n

            a, b = 1, 2

            for _ in range(3, n+1):
                a,b = b, a+b

            return b



            
        
