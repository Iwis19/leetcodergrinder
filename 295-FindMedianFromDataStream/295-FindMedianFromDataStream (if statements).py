from heapq import heappush, heappop

class MedianFinder:

    """
    i originally had a manual 1 way heappush sol and realized it didnt check which heap the new num would be inserted into and created
    unordered heaps... realized the issue and tried to patch. had to look at solution, but didnt really  understand solution vers so i went back 
    to read more solutions and implemented my own vers for that same bug from hte start on my own !

    160 ms runtime beats 76%
    """

    def __init__(self):
        self.left = []   # keeps the nums smaller than the (imaginary) median, closest to median (biggest) at the top
        self.right = []   # keeps the nums bigger than the (imaginary) median, closest to median (smallest) at the top

    def addNum(self, num: int) -> None:
        # append to left first, KEEP IT IN A WAY THAT ONLY LEFT CAN BE 1 BIGGER, NEVER RIGHT SIZE > LEFT SIZE
        if not self.left:
            heappush(self.left, -num)
            return

        if num > -self.left[0]:
            heappush(self.right, num)
        else:
            heappush(self.left, -num)
        
        if len(self.right) > len(self.left):
            heappush(self.left, -heappop(self.right))
        elif len(self.left) > len(self.right) + 1:
            heappush(self.right, -heappop(self.left))

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        
        return -self.left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
