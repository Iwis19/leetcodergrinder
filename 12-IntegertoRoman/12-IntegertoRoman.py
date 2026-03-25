# Last updated: 3/25/2026, 1:14:15 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3
4        """
5        LEARNED from problem:
6        1. 
7
8        67 ms 
9        """
10
11        left = 0
12        right = len(height)-1
13        max_area = 0
14
15        while left < right:
16
17            area = min(height[left], height[right]) * (right - left)
18            max_area = max(max_area, area)
19
20            if height[left] >= height[right]: right -= 1
21            elif height[right] > height[left]: left += 1
22
23        return max_area
24
25
26        