# Last updated: 4/3/2026, 9:35:31 PM
1class Solution:
2    def triangleType(self, nums: List[int]) -> str:
3        
4        if nums[0] >= nums[1] + nums[2] or nums[1] >= nums[0] + nums[2] or nums[2] >= nums[0] + nums[1]:
5            return "none"
6
7        if nums[0] == nums[1] == nums[2]:
8            return "equilateral"
9        if nums[0] == nums[1] or nums[1] == nums[2] or nums[2] == nums[0]:
10            return "isosceles"
11        else:
12            return "scalene"