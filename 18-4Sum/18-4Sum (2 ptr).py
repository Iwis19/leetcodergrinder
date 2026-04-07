class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        """
        sort the nums array
        two pointer to solve 2 sum
        outer loop to solve 3 sum
        outer outer loop to solve 4 sum

        1. overall good idea of the inner nested loops and bounds
        2. forgot about duplicate and setting logic for moving past
        - such as: changing l, r index when found a valid quadruple, skipping over i or j when same as prev (i-1) or (r+1)
        
        292 ms runtime beats 85%
        """

        nums.sort()
        l = len(nums)

        res = []

        #length 5: 0 1 2 3 4 e.g. i could be 0, 1, it needs at least 2 3 4 to scan through and find a possible [a,b,c]
        for i in range(l-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            sum3 = target - nums[i]

            #when i = 0, remaining arr could be 1 2 3 4
            #when i = 1, remaining arr could be 2 3 4

            #length 5: 0 1 2 3 4
            #i = 1, j = 2, j could only max 2 and no more after since we need 3 4 to at least form a pair to check
            #i = 0, j = 1, 2, remaining arr could be 2 3 4 or 3 4 
            for j in range(i+1, l-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                sum2 = sum3 - nums[j]

                #2 3 4 must hit sum2
                left, right = j+1, l-1

                while left < right:
                    sum = nums[left] + nums[right]
                    if sum == sum2: 
                        res.append(sorted([nums[i], nums[j], nums[left], nums[right]]))
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1

                    elif sum > sum2:
                        right -= 1
                    elif sum < sum2:
                        left += 1
                
        return res
        
