# Last updated: 3/27/2026, 6:04:58 PM
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        n = len(nums)

        for i in range(n - 2):
            seen = set()
            target = -nums[i]

            for j in range(i + 1, n):
                complement = target - nums[j]
                if complement in seen:
                    res.add(tuple(sorted((nums[i], nums[j], complement))))
                seen.add(nums[j])

        return [list(t) for t in res]