# Last updated: 3/25/2026, 1:13:49 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3
4        left = 0
5        right = len(height)-1
6        max_area = 0
7
8        while left < right:
9
10            area = min(height[left], height[right]) * (right - left)
11            max_area = max(max_area, area)
12
13            if height[left] >= height[right]: right -= 1
14            elif height[right] > height[left]: left += 1
15
16        return max_area
17
18
19        