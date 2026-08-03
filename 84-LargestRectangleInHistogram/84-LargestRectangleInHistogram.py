class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        """
        keep adding every bar into the stack

        once a lower bar is met, before appending the new bar, i would pop the most recent bar from the stack, calculate its area, repeat
        until all taller bars are removed, then add the new bar.

        this question was out of the ordinary for me tbh. my original thought process was honestly nowhere close and thought i had to use a deque (like the buy / sell stocks question) in a single pass.

        this solution is pretty interesting.

        i originally thought that it was more like i keep adding hte pillars until it is lower than the previous one (somewhat close), and then i would keep tracking the shortest bar, and then at some certain condition i would calculate it, and then popleft() on the leftmost bars until
        all of the ______ (didnt think this through) were removed.

        118 ms beats 62%
        """

        res = -1
        stack = []   # is supposed to store tuples: (index, height)

        for i, height in enumerate(heights):
            start = i  # at height <height>, a rectangle is allowed and is able to originally start at its own position.

            while stack and stack[-1][1] >= height:
                old_i, old_height = stack.pop()
                res = max(res, (i - old_i) * old_height)   # this is to calculate areas like test case #1 for [5, 6]. this works because it doesnt have to worry about any heights below it as they cannot exist in this stack already due to the loop logic. from the current point to the original location of the bar, this rectangle forms and works.
                start = old_i     # as i pop these pillars, the start index for which this current height <height> can create a rectangle of <height> from is updated. this works because once the taller bars are removed, and there are only bars shorter than <height>, we cant extend this rectangle anymore.

            stack.append((start, height))

        n = len(heights)

        for i, height in stack:
            res = max(res, (n-i) * height)  # the remaining pieces in the stack would work from <start> to the end of the heights array, hence n - i and multiplied by the height saved.

        return res







