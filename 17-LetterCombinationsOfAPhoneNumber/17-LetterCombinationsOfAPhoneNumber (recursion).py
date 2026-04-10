class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        """
        1. recursion method, learned this: WE USE combo[:] BECAUSE IT CREATES A COPY OF COMBO, OR ELSE WHEN COMBO IS UPDATED, COMBO IN RES ALSO CHANGES

        0 ms runtime beats 100
        """

        if not digits: return []

        map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }


        #recursion backtracking

        #id: current index of digit being processed in the digits string - we begin on 0
        #combo: the current combination being formed by appending letters - we begin at an empty str

        #first checks base case if id is equal to length of digits, if it is, it ap pends the current combo to the result arr
        # - WE USE combo[:] BECAUSE IT CREATES A COPY OF COMBO, OR ELSE WHEN COMBO IS UPDATED, COMBO IN RES ALSO CHANGES

        #if not, iterate through each letter corresponding to that digit
        #for each letter, recursively call backtrack with id+1 to process the next digit

        def backtrack(i, combo):

            if i == len(digits):
                res.append(combo[:])
                return

            for letter in map[digits[i]]:
                backtrack(i + 1, combo+letter)

        res = []
        backtrack(0, "")
        
        return res
