# Last updated: 3/26/2026, 10:34:15 PM
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:


        """
        0-3 ms runtime beats 100% | 19 mb memory beats 47%
        """
        output = []


        nums.sort()
        heapify(nums)


        while nums:
            alice = heappop(nums)
            bob = heappop(nums)


            output.append(bob)
            output.append(alice)


        return output


