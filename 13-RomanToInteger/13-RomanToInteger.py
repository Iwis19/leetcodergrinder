class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {"I":1, "V":5,  "X":10, "L":50,  "C":100, "D":500,  "M":1000}

        #idk this solution is honestly like too messy
        output = numbers[s[-1]]
        
        for i in range(len(s)-2, -1, -1):
            if numbers[s[i]] < numbers[s[i+1]]:
                output -= numbers[s[i]]
            else:
                output += numbers[s[i]]

        return output

