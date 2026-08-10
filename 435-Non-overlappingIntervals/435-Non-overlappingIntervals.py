class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        res = 0
        intervals.sort(key=lambda x:x[1])

        """
        **original thought process:

        since sorted, i dont have to worry about the 1st number in each tuple being non-connected

        i also do not have to worry about the list selection as it could either be 1,3 3,4 or 1,2 2,3 3,4 since we want minimum removed not minimum kept

        cases: (assuming we can definitely FORM a interval w given intervals)
            1. prev_end is greater than curr_start -> +1 to res
            2. prev_end is smaller than curr_start -> +1 to res
            3. prev_end is equal to curr_start -> proper case
        
        **final solution:

        ABOVE SOLUTION ONLY WORKS WHEN IT IS SORTED BY 1ST INDEX ELEMENT OF EACH TUPLE, why??
        
        i want max number of non overlapping intervals, for that, i need intervals to end as early as possible before the next interval starts. pretty much the same as my 2nd pt in the original thought process

        if i sort by first element, i have non overlapping intervals which wont be maximum, which in turn will result in my result not being minimum despite being a valid result for removal.

        test on [ [1,100] , [11,22] , [1,11] , [2,12] ]

        68 ms runtime beats 77%
        """

        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if prev_end > intervals[i][0]:
                res += 1
            else:
                prev_end = intervals[i][1]

        return res

