class Solution:
    def toLowerCase(self, s: str) -> str:

        """
        remember theres no difference between char and str in python since hteres no built in types thios way
        """

        res = ""
        
        for char in s:
            if char.isupper():
                res += chr(ord(char) + 32)
            else:
                res += char

        return res
