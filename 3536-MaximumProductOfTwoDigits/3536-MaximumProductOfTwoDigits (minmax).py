class Solution:
    def maxProduct(self, n: int) -> int:

        """
        did this at the end after seeing 7/26 daily msol

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
            
