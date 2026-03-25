# Last updated: 3/24/2026, 11:55:02 PM
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        
        """
        LEARNED from problem:
        1. I used the brute force option, time complexity is O(max(num1,num2)), leads to too many subtractions when numbers are very large
        2. optimized approach is the euclidean algorithm: subtracting num2 from num1 repeatedly until num1 < num2 is equivalent to doing num1 // num2 times in one go, essentially gcd algorithm but sums up all quotients

        41 ms runtime beats 63.31% | 19.22 mb memory beats 80%
        """

        ctr = 0

        while num1 and num2:

            if num1 >= num2: 
                num1 -= num2
            elif num2 > num1: 
                num2 -= num1

            ctr+=1

        return ctr