class Robot:


    """
    didnt really realize that the robot only moves along the perimeter, idk how i missed that (since it only turns when it meets bounds, it must be walking @ perimeter since it starts in a corner)

    calculat perimeter cuz (width-1) + (height-1) + (width-1) + (height-1) 
    """


    def __init__(self, width: int, height: int):
        self.dir = 1
        self.pos = [0,0]
        self.w = width
        self.h = height
        self.move = [[0,1], [1,0], [0,-1], [-1,0]]
        self.perimeter = 2 * (self.w + self.h) - 4


    def step(self, num: int) -> None:
        x,y = self.pos
       
        num %= self.perimeter
        if num == 0:
            num = self.perimeter

        while num > 0:
            nx = x + self.move[self.dir][0]
            ny = y + self.move[self.dir][1]

            if nx < 0 or nx >= self.w or ny < 0 or ny >= self.h:
                self.dir = (self.dir - 1) % 4
                continue

            x,y = nx, ny
            num -= 1
       
        self.pos = [x,y]


    def getPos(self) -> List[int]:
        return self.pos


    def getDir(self) -> str:
        if self.dir == 0: return "North"
        if self.dir == 1: return "East"
        if self.dir == 2: return "South"
        if self.dir == 3: return "West"




# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

