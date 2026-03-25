# Last updated: 3/25/2026, 3:26:10 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3
4        if len(s) <= 1: return s
5
6        ans = s[0]
7
8        i = 0
9        l = len(s)
10
11        def expand_from_center(left,right):
12            while right < l and left > -1 and s[left] == s[right]:
13                left -= 1
14                right += 1
15            return s[left+1:right]
16
17        for i in range(l-1):
18
19            #aba case
20            odd = expand_from_center(i,i)
21            #abba case (start on left b) (or right b)
22            even = expand_from_center(i,i+1)
23
24            if len(odd) > len(ans): 
25                ans = odd
26            if len(even) > len(ans): 
27                ans = even
28
29        return ans
30
31
32
33            
34        