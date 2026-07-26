class Solution:
    def maxProduct(self, n: int) -> int:

        """
        geeg bro i am trash now after like 3 weeks

        took a long time but in my defence i was not locked in and i was looking at keyboards

        realized to use a dq myself, took some time to think of how to select top 2 digits while saving some tc / computations

        in solutions, i like the freq array the most, will try do to that now !

        ADDED NOTE: good to note that n itself is positive , the nature of this question eliminates the possibility of negative x negative for an extra case

        no more dq ! even tho tc is down this is cleaner

        0 ms runtime beats 100%
        """
        
        l = int(math.log(n, 10)) + 1
        a, b = -1, -1

        for _ in range(l):
            dig = n % 10
            n //= 10

            ta = a

            a = max(a, dig)
            b = max(b, min(ta, dig))

        return a * b
            
