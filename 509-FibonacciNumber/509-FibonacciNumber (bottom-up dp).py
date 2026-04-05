class Solution:
    def fib(self, n: int) -> int:

        memo = {}

        if n == 0: return 0

        for i in range(1, n+1):

            if i <= 2:
                memo[i] = 1
            else:
                memo[i] = memo[i-2] + memo[i-1]

            
        return memo[n]
        
