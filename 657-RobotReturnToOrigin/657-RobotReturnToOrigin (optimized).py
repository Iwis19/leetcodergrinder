class Solution:
    def judgeCircle(self, moves: str) -> bool:

        """
        1. GOOD SOLUTION WITH COUNTER, i like this.

        7 ms beats 81%
        """

        freq = Counter(moves)

        return (freq["L"] == freq["R"]) and (freq["U"] == freq["D"])
        
