class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        element = 0
        digit = 0

        def digit_sum(num):

            res = 0

            while num > 0:
                res += num%10
                num //= 10

            return res

        for num in nums:
            element += num
            digit += digit_sum(num)

        return abs(element-digit)
