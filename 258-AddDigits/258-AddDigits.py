# Last updated: 3/26/2026, 8:36:51 PM
class Solution:
    def addDigits(self, num: int) -> int:

        """
        LEARNED from problem:
        1. i should try coding fully fully working solutions for every problem from now on, consider what im missing, logic errors, etc

        0 ms runtime beats 100% | 19 mb memory beats 75%
        """

        string = str(num)

        while len(string) > 1:
            sum = 0
            for char in string:
                sum += int(char)
            string = str(sum)
        
        return int(string)