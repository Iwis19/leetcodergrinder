# Last updated: 3/26/2026, 10:07:08 PM
import math

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:

        """
        LEARNED from problem:
        1. forgot that pop takes in index and not element
        2. not very efficient as nums.index gives O(n) inside O(n) loop, making O(n^2)

        11 ms runtime beats 7% | 19 mb memory beats 47%
        """

        res = []

        def findMinIndex(nums: List[int]) -> int:

            res = math.inf
            for num in nums:
                res = min(num, res)

            return nums.index(res)

        while nums:
            
            alice = nums.pop(findMinIndex(nums))
            bob = nums.pop(findMinIndex(nums))
            
            res.append(bob)
            res.append(alice)

        return res



        
