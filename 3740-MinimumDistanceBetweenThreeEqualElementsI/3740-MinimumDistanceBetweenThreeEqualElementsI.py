class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        """
        was kind of lost tbh

        1. had an idea of using a map to store the indices of each distinct numbers
        2. but forgot values() existed but i def need to rmb it more, including items() and keys()
        3. was lost on how to keep track if i even have 3 valid good values to find closest dist, thought abt using a separate var, but this is more efficient

        saw from a discussion, kind of a math probloem actually:
        - sorted indices for example a,b,c where a<b<c:
        - (a-b) + (b-c) + (c-a)
        - (b-a) + (c-b) + (c-a)
        - b + c + c - a - b - a
        - 2c - 2a
        - 2(c-a)

        0 ms runtime beats 100
        """
        
        good = {}

        for i in range(len(nums)):

            num = nums[i]
            if num not in good:
                good[num] = [i]
            else:
                good[num].append(i)

        min_dist = math.inf

        for arr in good.values():
            
            if len(arr) < 3: continue

            for i in range(len(arr)-2):
                dist = 2*(arr[i+2] - arr[i])
                min_dist = min(min_dist,dist)

        return -1 if min_dist == math.inf else min_dist





