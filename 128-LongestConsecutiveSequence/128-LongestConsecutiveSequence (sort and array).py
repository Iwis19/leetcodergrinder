class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        """
        this was my initial solution, i know its O(nlogn) and i shouldve known earlier

        1. originally missed edge case (nums length = 0) on my first submit
        2. put in max(res, temp) but initially forgot to just return max(res,temp) to account for the final answer

        43-59 ms runtime beats 85%
        """
        
        if not nums: return 0

        nums.sort()

        res = 1
        temp = 1

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            elif nums[i] == nums[i+1] - 1:
                temp += 1
            else:
                res = max(res, temp)
                temp = 1

        return max(res, temp)
