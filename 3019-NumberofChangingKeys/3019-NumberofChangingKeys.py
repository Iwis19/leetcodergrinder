# Last updated: 4/3/2026, 11:07:01 AM
1class Solution:
2    def countKeyChanges(self, s: str) -> int:
3        
4        s = s.lower()
5        res = 0
6
7        for i in range(len(s)):
8
9            if i != 0 and s[i-1] != s[i]:
10                res+=1
11
12        return res