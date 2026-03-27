# Last updated: 3/27/2026, 12:49:12 AM
class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        """
        1. wow i remembered sorted() !1!1
        """

        res, i = 0, 0
        expected = sorted(heights)

        while i < len(heights):

            if heights[i] != expected[i]:
                res+=1
            i+=1

        return res

        