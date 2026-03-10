class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        total = 0

        #i first add all the values fround in the string, but then i find if the previous value was smaller, i take out the previous value twice
        for i in range(len(s)):
            total += values[s[i]]

            if i > 0 and values[s[i]] > values[s[i-1]]:
                total -= 2 * values[s[i-1]]

        return total
