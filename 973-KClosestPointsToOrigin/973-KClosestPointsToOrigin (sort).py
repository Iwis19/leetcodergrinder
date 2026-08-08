class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        """
        this was the first solution before heap

        83 ms runtime beats 21%
        """
        
        dists = []
        def dist(p,i):
            dists.append([math.sqrt(p[0]**2 + p[1]**2), i])

        for i, point in enumerate(points):
            dist(point, i)
            
        dists.sort()

        res = [ points[dists[i][1]] for i in range(k) ]

        return res

        

        
