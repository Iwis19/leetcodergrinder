class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        """
        origianlly used two for loops (1 for traaversing thru nums, 1 for going thru freq values), but realized on my own that it was not optimized
        """
        
        freq = {}

        for num in nums:
            if num in freq:
                return True
            freq[num] = 1

        return False
