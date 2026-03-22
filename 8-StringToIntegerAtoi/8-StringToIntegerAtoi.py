# Last updated: 3/22/2026, 6:09:02 PM
class Solution:

    """
    LEARN from solution:
    1. i used a helper function :)
    2. learned a method: lstrip() -> strips leading whitespaces, rstrip() -> strips trailing whitespaces, strip() does both
    3. consider edge cases, sequencing is very important
    4. how to clamp numbers with min , max. -> max(INT_MIN, min(INT_MAX, myInput))
    5. use ord() for ascii better

    3 ms runtime beats 36% |  19 mb memory beats 91%
    O(N^2)....
    """
    
    #checks string version
    def isNumber(self, s:str) -> bool:

        if len(s) != 1:
            return False
        if ord("0") <= ord(s) <= ord("9"):
            return True
        return False


    def myAtoi(self, s: str) -> int:

        s = s.lstrip()

        isNegative = False
        isLeadingZero = True
        numbers = ""
        if not s: return 0

        first = s[0]
        if (not self.isNumber(first)) and first != "-" and first != "+": return 0
        if first == "-": isNegative = True


        for i in range(0, len(s)):

            char = s[i]

            if i == 0 and (char == "-" or char == "+"):
                continue

            if not self.isNumber(char):
                break

            if int(char) == 0 and isLeadingZero:
                continue
            else:
                isLeadingZero = False
                numbers += char

        if not numbers:
            return 0
            
        numerical = int(numbers)

        if isNegative:
            numerical = -1*numerical 
        numerical = max(-2**31, min(numerical, 2**31-1))
        return numerical



