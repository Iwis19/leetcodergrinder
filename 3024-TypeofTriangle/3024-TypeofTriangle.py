# Last updated: 4/3/2026, 9:37:00 PM
1class Solution:
2    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
3        
4        res = []
5
6        for i, word in enumerate(words):
7
8            if x in word:
9                res.append(i)
10
11        return res