class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        """
        brute force solution, will do one with binary search after

        0ms runtime 100%
        """
        
        n = len(nums)

        if n == 1: return 0
        if nums[0] > nums[1]: return 0
        if nums[n-1] > nums[n-2]: return n-1

        for i in range(n):

            if (i+1 < n and nums[i] > nums[i+1]) and (i-1 >= 0 and nums[i] > nums[i-1]):
                return i

        return None
        
