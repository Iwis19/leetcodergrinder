# Last updated: 3/26/2026, 10:14:27 PM
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:

        """
        0-3 ms runtime beats 44% | 19 mb memory beats 79%
        """

        nums.sort()

        for i in range(0,len(nums),2):

            temp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = temp

        return nums

    



        