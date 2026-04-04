class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:

        """
        1. originally went for the sum of indices where the chars were the same, and then checked if that was 
        even or odd, if it was even, then its true, if not then its false, but eventually realized that sometimes 
        when chars were off by one each, then the sum would be 0 and it would still be counted as even... even tho it fails.

        0 ms beats 100
        """

        s1even = sorted([s1[0], s1[2]])
        s1odd = sorted([s1[1], s1[3]])
        s2even = sorted([s2[0],s2[2]])
        s2odd = sorted([s2[1],s2[3]])

        return s1even == s2even and s1odd == s2odd
        
