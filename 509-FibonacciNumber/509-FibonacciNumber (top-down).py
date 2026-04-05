class Solution:
    def fib(self, n: int) -> int:

        """
        1. it was a bery good dp practice

        i go from fib(n) -> fib(n-1) -> ... -> fib(1) instead of the other way around
        also with memoization (makes it so that i dont have to recompute repeating values everytime)
        """

        memo = {}

        def dp(n):
            if n in memo:
                return n
            if n == 0:
                return 0
            if n <= 2:
                return 1
            
            memo[n] = dp(n-1) + dp(n-2)
            return memo[n]

        return dp(n)
        
