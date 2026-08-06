class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        """
        mmm did too much swift i thought i could place the nested func under the loop :(
        
        0 ms runtime beats 100%
        """
    
        def product(n: int) -> int:
            res = 1

            while n:
                res *= (n % 10)
                n //= 10

            return res

        while product(n) % t:
            n += 1

        return n


        
