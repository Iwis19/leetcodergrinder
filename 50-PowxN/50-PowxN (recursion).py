class Solution:
    def myPow(self, x: float, n: int) -> float:

        """
        even though i dont get how it works, im going to keep it here and give ane xplanation:

        base case: if n == 0, then return 1 since anything to pow of 1 is 1.0
        negative exponent: if n is negative, we must work on the reciprocal of base which is 1/x and making the exponent positive, hence -n
        recursion:
        - n is even: make expression (x*x)^(n/2)
        - n is odd: pull out one x: x*(x*x)^[(n-1)/2]

        but in python, n//2 handles n/2 same as (n-1)/2 so we may do n/2 instead of that.

        what i was confused about: why bother dividing n by 2?
        normally: 2^8 -> power goes from 8 7 6 5 4 3 2 1 -> 8 steps
        this way: 2^8 -> power goes from 8 4 2 1 0 -> 5 steps O(logn)
        """
      
        if n == 0:
            return 1

        if n < 0:
            return self.myPow(1/x, -n)

        if n%2 == 0:
            return self.myPow(x*x, n//2)

        elif n%2 == 1:
            return x*self.myPow(x*x, n//2)
