# Last updated: 4/3/2026, 11:02:11 AM
1class Solution:
2    def differenceOfSums(self, n: int, m: int) -> int:
3        
4        num1 = 0
5        num2 = 0
6
7        for i in range(1,n+1):
8            if i % m != 0:
9                num1 += i
10            else:
11                num2 += i
12
13        return num1 - num2
14
15        