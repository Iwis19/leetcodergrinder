# Last updated: 3/26/2026, 11:10:36 PM
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        """
        1. amazing problem, had stupid poop mistakes (did a for index loop and not for element loop thinking it was a for element loop and accessing sentence)

        0-4 ms runtime beats 100%
        """

        res = -1
        for sentence in sentences:
            words = sentence.split(" ")
            res = max(len(words), res)

        return res