class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        """
        1. not optimal. is O(n^2) time but takes much more time and space as i splice every single loop, failed on test case with arrays of 0s
        2. this approach can however still be optimized to pass the test
        3. i will try again
        """

        res = set()

        def solve_two_sum(nums: list[int], target: int) -> list[int]:
            map = {}
            results = []
            for i, num in enumerate(nums):
                complement = target - num
                if complement in map:
                    results.append([complement, num])
                map[num] = i
            return results

        for i in range(len(nums)-2):

            #only have to scan forward arr because i wouldve already scanned the previous parts in prev loops
            complement_arr = nums[i+1:]
            target = -nums[i]
            outputs = solve_two_sum(complement_arr, target)
            for output in outputs:
                temp = tuple(sorted([nums[i], output[0], output[1]]))
                res.add(temp)

        return [list(threes) for threes in res]


           


   
       

