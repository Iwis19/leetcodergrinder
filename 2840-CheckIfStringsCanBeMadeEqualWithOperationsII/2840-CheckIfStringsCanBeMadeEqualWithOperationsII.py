class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        
        """
        1. learned a new way of checking even or odd: i & 1 is the same as i % 2 == 1

        checks bit by bit: for example, i == 10:

          1010
        & 0001
        _______
          0000

        then the result is 0, so the if statement does not run and goes to else.

        if i == 9:

          1001
        & 0001
        ______
          0001

        then result is 1, if statement runs.

        2. could also use hash map, which is O(n) and O(1) time and space respectively, currently is O(nlogn), O(n)

        
        """

        even1, even2, odd1, odd2 = [], [], [], []

        for i in range(len(s1)):
            if i%2 == 0:
                even1.append(s1[i])
                even2.append(s2[i])
            else:
                odd1.append(s1[i])
                odd2.append(s2[i])

        return sorted(even1) == sorted(even2) and sorted(odd1) == sorted(odd2)
