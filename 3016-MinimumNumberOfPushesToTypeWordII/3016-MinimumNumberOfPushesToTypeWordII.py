class Solution:
    def minimumPushes(self, word: str) -> int:

        """
        WTF HOW IS COUNT SO MUCH MORE EFFICIENT THAN A NORMAL O(N) LOOP???? this is lidelly O(26N) man

        18 ms ru ntime beats 99%, using normal count is 300 ms
        """

        freq = [word.count(chr(ord('a') + i)) for i in range(26)]

        freq.sort(reverse=True)

        res = 0

        for i, f in enumerate(freq):
            if not f: return res

            """
            0 -> 7: 1 click
            8 -> 15: 2 click
            16 -> 23: 3 click
            """

            res += f * (1 + i // 8)

        return res
