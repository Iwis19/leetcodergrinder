class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        """
        idk how this was diff from the last one but ig i learned
        
        335 ms runtime bneats 67
        """
        
        map = {}

        for i in range(len(nums)):

            num = nums[i]
            if num not in map:
                map[num] = []
            map[num].append(i)

        min_dist = math.inf

        for arr in map.values():

            if len(arr) < 3: continue
            for i in range(len(arr)-2):
                dist = 2*(arr[i+2] - arr[i])
                min_dist = min(dist, min_dist)

        
        return -1 if min_dist == math.inf else min_dist
