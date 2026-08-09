from heapq import heappush, heappop

class MedianFinder:

    """
    212 ms runtime beats 30%, need to come back to this to read a bit more, mostly makes sense tho in addNum
    """

    def __init__(self):
        self.left = []   # keeps the nums smaller than the (imaginary) median, closest to median (biggest) at the top
        self.right = []   # keeps the nums bigger than the (imaginary) median, closest to median (smallest) at the top

    def addNum(self, num: int) -> None:
        # append to left first, KEEP IT IN A WAY THAT ONLY LEFT CAN BE 1 BIGGER, NEVER RIGHT SIZE > LEFT SIZE
        heappush(self.left, -num)
        heappush(self.right, -heappop(self.left))
        if len(self.right) > len(self.left):
            heappush(self.left, -heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        
        return -self.left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
