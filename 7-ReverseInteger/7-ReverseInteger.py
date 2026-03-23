# Last updated: 3/23/2026, 3:14:00 PM
class Solution:
    def reverse(self, x: int) -> int:

        """
        LEARNED from solution:
        actualyl not a bad solution, learned from 8.atoi about dealing with clamping and traversing through i think
        1. my chud head didnt think that i could scan negative sign and then move i to 1 more
        2. using power was a good idea i liked it

        43 ms runtime beats 75% | 19 mb memory beats 85%
        """
        
        s = str(x)

        output = 0
        i = 0
        power = 0
        isNegative = False

        if s[0] == "-":
            i += 1
            isNegative = True

        while i < len(s):

            digit = int(s[i])
            output += digit * (10**power)

            if output > 2**31-1: return 0
            if output < -2**31: return 0
            power += 1
            i += 1

        output = output * -1 if isNegative else output
        return output


        
        
