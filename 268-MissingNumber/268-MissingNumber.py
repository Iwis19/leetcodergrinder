class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        """
        3 ms runtime beats 60%
        """
        
        seen = set()

        for num in nums:
            seen.add(num)

        i = 0

        while i in seen:
            i += 1

        return i
            
