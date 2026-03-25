# Last updated: 3/25/2026, 3:29:16 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3
4        """
5        good things i did:
6        1. i came up with looping thru and expanding from middle myself (main idea)
7        2. i considered even and odd cases, even tho i didnt call them that, i said aba and abba
8        3. i wrote a while loop about expanding from middle
9
10        learned:
11        1. needed some help on implementation
12        2. shouldve thought about using an inner function to make solution simpler
13        3. some indexing issues 
14        4. originally thought i had to consider abba where im the left b and abba where im the right b but realized i move onto the next b regardless
15
16        211 ms runtime beats 92% | 19 mb memory beats 60%
17        """
18
19        if len(s) <= 1: return s
20
21        ans = s[0]
22
23        i = 0
24        l = len(s)
25
26        def expand_from_center(left,right):
27            while right < l and left > -1 and s[left] == s[right]:
28                left -= 1
29                right += 1
30            return s[left+1:right]
31
32        for i in range(l-1):
33
34            #aba case
35            odd = expand_from_center(i,i)
36            #abba case (start on left b) (or right b)
37            even = expand_from_center(i,i+1)
38
39            if len(odd) > len(ans): 
40                ans = odd
41            if len(even) > len(ans): 
42                ans = even
43
44        return ans
45
46
47
48            
49        