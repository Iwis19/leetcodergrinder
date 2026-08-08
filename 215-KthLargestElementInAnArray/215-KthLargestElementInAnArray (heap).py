from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        """
        pretty basic heap exercise good one

        had some brain farts + also thought you can do a maxheap straight up, need some more syntax training

        108 ms runtime beats 28%, might do quickselect

        the stupid sort submissions make it look slow but fudge these guys
        """
        
        l = len(nums)

        nums = [ -num for num in nums ]
        heapify(nums)
        
        for i in range(k - 1):
            heappop(nums)

        return -heappop(nums)
