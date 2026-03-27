# Last updated: 3/27/2026, 1:44:32 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        
4        map = {}
5
6        for i,num in enumerate(nums):
7            map[num] = i
8
9        for index, current in enumerate(nums):
10
11            complement = target - current
12            if complement in map and index != map[complement]:
13
14                return [index, map[complement]]
15
16        return []
17