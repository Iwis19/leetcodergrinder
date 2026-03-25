# Last updated: 3/25/2026, 10:47:56 AM
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        """
        LEARNED from problem:
        1. this is the solution i was thinking about, i like this a lot more than the other one
        2. took some time to think about the math but it was cool i liked it
        3. overall had some minor bugs and careless mistakes but ultimately debugged

        NEED TO WORK ON: logic operator i often misuse OR and AND

        8 ms runtime beats 72% | 19 mb memory beatss 70%
        """

        results = ""
        l = len(s)
        cycle = 2*numRows - 2

        if numRows == 1: return s

        for r in range(numRows):

            index = r
            while index < l:
                results += s[index]

                if r != 0 and r != numRows-1:
                    space = 2*(numRows - (r+1))
                    if index+space < l:
                        results += s[index+space]

                index += cycle

        return results
