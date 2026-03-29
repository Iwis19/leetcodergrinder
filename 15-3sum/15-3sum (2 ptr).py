class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        res = set()

        def all_two_sum(arr, target):

            left = 0
            right = len(arr)-1

            res = set()

            while left < right:

                sum = arr[left] + arr[right]
                if sum == target:
                    res.add((arr[left], arr[right]))
                    left += 1
                    right -= 1
                elif sum < target:
                    left += 1
                elif sum > target:
                    right -= 1

            return [list(r) for r in res]
        
        for i, num in enumerate(nums):

            target = -num
            remaining = nums[i+1:]
            results = all_two_sum(remaining, target)
            for result in results:
                res.add((num, result[0], result[1]))
            
        return [list(r) for r in res]




