# Last updated: 3/27/2026, 1:48:13 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        
4        """
5        1. two pass hash is used here, but one pass hash also works here because if i was on index 0 and the valid complement was index 2, i dont need to worry that i didnt find it as ill see my index 0 in my hash when im at index 2
6        """
7
8        map = {}
9
10        for i,num in enumerate(nums):
11            map[num] = i
12
13        for index, current in enumerate(nums):
14
15            complement = target - current
16            if complement in map and index != map[complement]:
17
18                return [index, map[complement]]
19
20        return []
21