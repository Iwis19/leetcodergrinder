# Last updated: 3/27/2026, 12:51:20 AM
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        
        alice, bob = 0, 0

        for num in nums:

            if num >= 10: alice+=num
            else: bob+=num

        return alice != bob
