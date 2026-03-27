# Last updated: 3/27/2026, 3:25:20 PM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        res = set()
4        n = len(nums)
5
6        for i in range(n - 2):
7            seen = set()
8            target = -nums[i]
9
10            for j in range(i + 1, n):
11                complement = target - nums[j]
12                if complement in seen:
13                    res.add(tuple(sorted((nums[i], nums[j], complement))))
14                seen.add(nums[j])
15
16        return [list(t) for t in res]