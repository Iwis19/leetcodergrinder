class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:

        """
        very happy with myself :)

        111 ms beats 70
        """

        s = []
        
        #append all into an arr, then join(), then rstrip() the final string

        if rows == 1: return encodedText

        cols = len(encodedText) // rows

        #col number
        c = 0

        for c in range(cols):
            tempr = 0
            tempc = c

            while tempc < cols and tempr < rows:
                s.append(encodedText[tempr*cols+tempc])
                tempc += 1
                tempr += 1
            
            c += 1

        string = "".join(s)

        return string.rstrip()
            
