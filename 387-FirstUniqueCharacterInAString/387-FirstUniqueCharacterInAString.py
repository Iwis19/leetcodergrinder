# Last updated: 3/26/2026, 9:56:56 PM
class Solution:
    def firstUniqChar(self, s: str) -> int:

        """
        LEARNED from problem:
        1. i dont always have to look for the MOST efficient solution. I can just map out all of my thoughts.
        2. i definitely need to improve on thinking about my time efficiency i lowkey get my own solutions time efficiency wrong
        3. anyways, good question to brush up on my dict syntax

        61 ms runtime beats 67% | 19 mb memory beats 48%
        """

        freq = {}

        for char in s:
            freq[char] = freq.get(char,0)+1

        for i in range(len(s)):
            char = s[i]
            if freq[char] == 1:
                return i

        return -1

            
        