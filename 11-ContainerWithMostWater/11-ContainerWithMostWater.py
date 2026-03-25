# Last updated: 3/25/2026, 1:36:48 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:

        """
        1. didnt have a clue on how to solve this, thought about two pointer but i thought it wouldnt work since i thought 
        it would miss out on the future best cases
        2. i originally had a solution where it kept track of max height column, and calculated area with it with the 
        current column i was on from a few weeks back, so it was good i thought about two pointer at least

        LOGIC LEARNED:
        - either certainly decrease the area by moving the taller column closer to center, as the width already decreases
        - or maybe increase the area by moving the shorter column closer to center, altho width decreases

        this is a GREEDY solution, and it works here because the locally optimal outcome doesnt mess up the optimal
        future outcome like i said in pt 1

        55 ms runtime beats 73% | 29 mb memory beats 80%
        """

        left = 0
        right = len(height)-1
        max_area = 0

        while left < right:

            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] >= height[right]: right -= 1
            elif height[right] > height[left]: left += 1

        return max_area


        