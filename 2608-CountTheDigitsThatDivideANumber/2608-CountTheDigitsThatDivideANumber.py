# Last updated: 3/27/2026, 12:38:04 AM
class Solution:
    def countDigits(self, num: int) -> int:

        """
        1. used num > 10 instead of num > 0 that was a poop mistake on me tbh

        0 ms runtime beats 100% O(n)
        """

        if num < 10: return 1
        
        res = 0
        number = num
        
        while num > 0:

            digit = num % 10
            if number % digit == 0:
                res += 1

            num //= 10
        
        return res
