class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        """
        i liked this problem

        1. i very much like how my mind defaulted to using a dict
        2. my brain died and had a bit of struggles on making the actual algorithm
        - missed the empty str starting in res
        - took too long to think about the loopings and required a peek at answer

        0 ms runtime beats 100
        """

        if not digits: return []

        map = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        res = [""]

        #go thru each digit (for loop)

        #as i go thru, i access the string in map, and for loop on its length to append into the array 1 by 1

        for digit in digits:

            new_res = []
            letters = map[int(digit)]

            for letter in letters:

                for combo in res:
                    new_res.append(combo+letter)

            res = new_res

        return new_res
