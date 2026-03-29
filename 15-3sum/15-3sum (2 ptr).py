class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        res = []

        def all_two_sum(arr, target):

            left = 0
            right = len(arr)-1

            res = []

            while left < right:

                sum = arr[left] + arr[right]
                if sum == target:
                    res.append([arr[left], arr[right])
                    left += 1
                    right -= 1
                elif sum < target:
                    left += 1
                elif sum > target:
                    right -= 1

            return res
        
        for i, num in enumerate(nums):

            target = -num
            remaining = nums[i+1:]
            results = all_two_sum(remaining, target)
            for result in results:
                res.append([num, result[0], result[1])
            
        return res




