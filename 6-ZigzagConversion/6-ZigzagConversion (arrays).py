# Last updated: 3/25/2026, 10:26:13 AM
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        """
        LEARNED from problem:
        1. I definitely had a bit of trouble comprehending this problem since the zigzag wasnt ssuper clear to me
        2. I initially wanted to create a solution by noticing index patterns for each row which i will probably try out now
        3. While looking through the discussions of how zigzag works, i saw this looping technique so i did not entirely come up with this myself
        4. I originally decided to find how many repeating patterns of zigzags there were (vertically), and then i woudl use another loop for the extras (not a filled zigzag), but it was unnecessary
        5. I forgot to track index bounds on my first attempt

        9 ms runtime beats 88% | 19 mb memory beats 91%
        """
        
        arr = [[] for _ in range(numRows)]
        output = ""
        l = len(s)
        index = 0

        while index < l:

            for j in range(numRows):
                if index < l:
                    arr[j].append(s[index])
                    index+=1
            for j in range(numRows-2, 0, -1):
                if index < l:
                    arr[j].append(s[index])
                    index+=1

        for row in arr:
            output += "".join(row)

        return output
