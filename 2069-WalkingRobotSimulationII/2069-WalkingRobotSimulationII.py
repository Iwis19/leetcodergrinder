# Last updated: 4/6/2026, 8:49:28 PM
1class Robot:
2
3    def __init__(self, width: int, height: int):
4        self.dir = 1
5        self.pos = [0,0]
6        self.w = width
7        self.h = height
8        self.move = [[0,1], [1,0], [0,-1], [-1,0]]
9
10    def step(self, num: int) -> None:
11        x,y = self.getPos()
12        cycle = 2 * (self.w + self.h) - 4
13        num %= cycle
14
15        if num == 0:
16            num = cycle
17
18        while num > 0:
19            nx = x + self.move[self.dir][0]
20            ny = y + self.move[self.dir][1]
21
22            if nx < 0 or nx >= self.w or ny < 0 or ny >= self.h:
23                self.dir = (self.dir - 1) % 4
24                continue
25
26            x,y = nx, ny
27            num -= 1
28        
29        self.pos = [x,y]
30
31
32    def getPos(self) -> List[int]:
33        return self.pos
34
35    def getDir(self) -> str:
36        if self.dir == 0: return "North"
37        if self.dir == 1: return "East"
38        if self.dir == 2: return "South"
39        if self.dir == 3: return "West"
40
41
42# Your Robot object will be instantiated and called as such:
43# obj = Robot(width, height)
44# obj.step(num)
45# param_2 = obj.getPos()
46# param_3 = obj.getDir()