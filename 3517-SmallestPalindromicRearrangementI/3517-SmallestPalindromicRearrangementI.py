class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        """
        woooo solved no help (1 search on syntax since i forgor if u could do string*number to repeat)

        384 ms runtime beats 21%, optimized tc, sc o(n)

        originally used a freq arr manually counted, now using a counter(s).

        UPDATED: 175 ms beats 73%
        """

        if len(s) == 1:
            return s
        
        alphabets = Counter(s)

        # if even, then i just go thru all the elements in the alphabets arr and then divide by 2 and work on it
        # if odd, as i go through elements in the alphabets arr, i note which ones are odd numbered and i add it to a temp array

        left = []
        unused = ""

        for i in range(26):
            char = chr(i + ord('a')) 
            if alphabets[char]:
                left.append(char * (alphabets[char] // 2))
                if not unused and alphabets[char] % 2:
                    unused = char

        left = "".join(left)

        return left + unused + left[::-1]

        
