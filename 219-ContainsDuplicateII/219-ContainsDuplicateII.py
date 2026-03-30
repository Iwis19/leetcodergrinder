# Last updated: 3/30/2026, 10:32:01 AM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        
4        freq = {}
5
6        for num in nums:
7            freq[num] = freq.get(num, 0) + 1
8
9        for value in freq.values():
10            if value > 1:
11                return True
12        
13        return False