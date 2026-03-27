# Last updated: 3/27/2026, 12:43:04 AM
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        """
        1. good string splice use i remember this now string == string[::-1]
        2. i liked the in sol function creation

        0ms runtime 100%
        """

        def isPalindromic(string:str) -> bool:

            return string == string[::-1] 

        for word in words:

            if isPalindromic(word):
                return word
        
        return ""

        
