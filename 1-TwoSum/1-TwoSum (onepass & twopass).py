# Last updated: 3/27/2026, 1:48:33 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        1. two pass hash is used here, but one pass hash also works here because if i was on index 0 and the valid complement was index 2, i dont need to worry that i didnt find it as ill see my index 0 in my hash when im at index 2
        """

        map = {}

        for i,num in enumerate(nums):
            map[num] = i

        for index, current in enumerate(nums):

            complement = target - current
            if complement in map and index != map[complement]:

                return [index, map[complement]]

        return []
