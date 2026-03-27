# Last updated: 3/27/2026, 12:45:41 AM
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:

        """
        why is this even a leetcode problem
        """

        res = 0

        for hour in hours:
            if hour >= target:
                res+=1
        
        return res