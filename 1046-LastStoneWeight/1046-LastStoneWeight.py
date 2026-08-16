from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        """
        another good heap practice, need to remember that heapify() returns None and just turns an array into a heap ds.

        0 ms runtime beats 100
        """
        
        heap = [ -stone for stone in stones ]
        heapify(heap)

        while len(heap) >= 2:
            first, second = -heappop(heap), -heappop(heap) # biggest, second biggest

            if first == second: continue

            heappush(heap, second - first)

        if not heap:
            return 0
        
        return -heap[0]
