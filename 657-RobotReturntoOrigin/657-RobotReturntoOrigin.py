# Last updated: 3/27/2026, 1:35:46 AM
1class Solution:
2    def judgeCircle(self, moves: str) -> bool:
3
4        """
5        1. GOOD SOLUTION WITH COUNTER, i like this.
6
7        7 ms beats 81%
8        """
9
10        freq = Counter(moves)
11
12        return (freq["L"] == freq["R"]) and (freq["U"] == freq["D"])
13        