class Solution:
    def smallestSubsequence(self, string: str) -> str:

        """
        had a hard time, will come back tot his one 100%

        had to look at solution

        0 ms runtime beats 100%
        """
        
        freq = Counter(string)
        a, s = [], set()                        

        for char in string:
            freq[char] -= 1

            # case 1: char is alr in the array, skip
            # case 2: char isnt in the array, and is greater than the last chars
            # case 3: char isnt in the array, but is smaller than last chars, so needs to get wiped to check -> keep removing if exists later

            if char in s: continue  # must continue first. if i do not continue befor ehte while loop but rather do "if char not in s", im letting the while loop run on this char, removing previous arrays for no benefit, but rather disruption

            # i only have the balls to remove and look for a better sequence only if this char thats getting removed has another occurence in the future.
            while a and char < a[-1] and freq[a[-1]]:  # if i do not continue before this while loop, example "cbaacabcaaccaacababa" will remove a "abc" for a "acb" for no reason
                s.remove(a.pop())  
        
            s.add(char)
            a.append(char)
                
        return "".join(a)
