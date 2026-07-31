class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        """
        actually a pretty smart solution from the editorial. would NOT have thought about this amazing sol. will redo this soon !

        0 ms runtime beats 100%, O(nlogn) for sort
        """
        
        sequence = "123456789"
        res = []
        l = len(sequence)

        for s in range(l):
            for e in range(s, l):
                num = int(sequence[s:e+1])
                if low <= num <= high:
                    res.append(num)

        res.sort()

        return res
