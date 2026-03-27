# Last updated: 3/26/2026, 10:51:42 PM
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        """
        LEARNED from problem:
        1. better this time at hashmaps lets go

        0-4 ms runtime beats 100% 
        """
        
        freqs = [0 for _ in range(26)]

        for char in sentence:
            freqs[ord(char) - ord("a")] += 1
        
        for freq in freqs:
            if freq == 0:
                return False

        return True