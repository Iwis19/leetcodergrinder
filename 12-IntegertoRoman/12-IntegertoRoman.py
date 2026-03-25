# Last updated: 3/25/2026, 1:36:38 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3
4        """
5        1. didnt have a clue on how to solve this, thought about two pointer but i thought it wouldnt work since i thought 
6        it would miss out on the future best cases
7        2. i originally had a solution where it kept track of max height column, and calculated area with it with the 
8        current column i was on from a few weeks back, so it was good i thought about two pointer at least
9
10        LOGIC LEARNED:
11        - either certainly decrease the area by moving the taller column closer to center, as the width already decreases
12        - or maybe increase the area by moving the shorter column closer to center, altho width decreases
13
14        this is a GREEDY solution, and it works here because the locally optimal outcome doesnt mess up the optimal
15        future outcome like i said in pt 1
16
17        55 ms runtime beats 73% | 29 mb memory beats 80%
18        """
19
20        left = 0
21        right = len(height)-1
22        max_area = 0
23
24        while left < right:
25
26            area = min(height[left], height[right]) * (right - left)
27            max_area = max(max_area, area)
28
29            if height[left] >= height[right]: right -= 1
30            elif height[right] > height[left]: left += 1
31
32        return max_area
33
34
35        