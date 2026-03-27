# Last updated: 3/27/2026, 12:56:26 AM
class Solution:
    def judgeCircle(self, moves: str) -> bool:

        """
        1. lowkey didnt think i could do pos == [0,0]

        22 ms beats 13%
        """

        pos = [0,0]

        for move in moves:

            if move == "L": pos[0] -= 1
            elif move == "R": pos[0] += 1
            elif move == "U": pos[1] += 1
            elif move == "D": pos[1] -= 1

        return pos == [0,0]

        