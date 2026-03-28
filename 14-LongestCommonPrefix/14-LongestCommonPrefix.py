class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        """
        1. i learned that python handles slicing very very safely. i can use weird indices and it would NEVER give an error unless i am syntactically wrong. therefore, i am able to simply *return res[:-1]* instead of *return res[:len(res)-1] if len(res) > 1 else ""*. i dont have to worry abt if length = 0.
        
        0 ms beats 100%
        """

        res = ""

        i = 0
        min_word_length = min(len(word) for word in strs)

        if len(strs) == 0: return res
        if len(strs) == 1: return strs[0]

        while i < min_word_length:
            res += strs[0][i]
            for string in strs:
                if string[:i+1] != res:
                    return res[:len(res)-1] if len(res) > 1 else ""
            i+=1

        return res
            

        
        
