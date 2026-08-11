class Solution:
    def missingInteger(self, nums: List[int]) -> int:

        """
        trash desc but i felt like the other vers i interpreted wouldve been a good practice lowkey

        0 ms runtime beats 100%
        """
        
        seen = set()
        
        for num in nums:
            seen.add(num)

        s = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                s += nums[i]
            else:
                break

        while s in seen:
            s += 1
        
        return s

        
