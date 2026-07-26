class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        """
        will def come back to this, i like this logic a lot mor ethan what i did yesterday in the 2 numbers

        31 ms runtime beats 15%, same idea as 0ms sol, but didnt use comparison ops manually, used max/min instead
        """
        
        a, b, c = -1001, -1001, -1001
        x, y = 1001, 1001

        for num in nums:
            ta, tb = a, b

            a = max(a, num)
            b = max(b, min(ta, num))
            c = max(c, min(tb, num))

            tx = x

            x = min(x, num)
            y = min(y, max(tx, num))

        return max(a * x * y, a * b * c)
