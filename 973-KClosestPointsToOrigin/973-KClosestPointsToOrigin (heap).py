from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        """
        originally solved in O(nlogn) with a array to keep everything, then sort, then grab res

        heap works at logn speed for operations, so its more like nlogk instead of nlogn

        there is still a faster way (quickselect) but will see later.
        """
        
        h = []

        for i, point in enumerate(points):
            d = math.sqrt(point[0] ** 2 + point[1] ** 2)
            heappush(h, (d,i))


        res = [ points[heappop(h)[1]] for _ in range(k) ]

        return res

        

        
