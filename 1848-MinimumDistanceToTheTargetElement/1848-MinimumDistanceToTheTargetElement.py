class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:

        """
        good thoughts happened

        solved in 1 minute

        0 ms runtime beats 100
        """
        
        res = math.inf


        for i in range(len(nums)):
            num = nums[i]
            if num == target:
                dist = abs(i - start)
                res = min(res, dist)


        return res
