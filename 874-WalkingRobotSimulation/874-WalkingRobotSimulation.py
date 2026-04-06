class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        """
        learned so much

        1. originally was going to use a dict for simple lookup for obstacles, while that was the right direction, set also uses the same hashing principle, and set just fits better generally here

        2. nonlocal: lets me edit variables from outer functions, i initially just assumed i could do it without this keyword...

        3. must add pairs into sets as tuples. since tuples are immutable, this would work. lists are mutable, so if i modify this list in a set, the "location" in the hash storage would break, meaning everything else such as lookup would also break.

        22-42 ms runtime beats 97%
        """
        
        obstacle_map = set()

        for x,y in obstacles:
            obstacle_map.add((x,y))

        direction = 0

        res = -1
        x,y = 0, 0

        def move(steps):
            nonlocal x,y

            for _ in range(steps):
                if direction == 0:  
                    if (x,y+1) in obstacle_map:
                        break
                    y += 1
                elif direction == 180:
                    if (x,y-1) in obstacle_map:
                        break
                    y -= 1
                elif direction == 90:
                    if (x+1,y) in obstacle_map:
                        break
                    x += 1
                elif direction == 270:
                    if (x-1,y) in obstacle_map:
                        break
                    x -= 1

        for command in commands:
            if command == -2:
                direction = (direction-90)%360
            elif command == -1:
                direction = (direction+90)%360

            if 1 <= command <= 9:
                move(command)

            res = max(res, x**2+y**2)

        return res
        
