class Solution:
    def maxProduct(self, n: int) -> int:

        """
        geeg bro i am trash now after like 3 weeks

        took a long time but in my defence i was not locked in and i was looking at keyboards

        realized to use a stack myself, took some time to think of how to select top 2 digits while saving some tc / computations

        in solutions, i like the freq array the most, will try do to that now !

        0 ms runtime beats 100%
        """
        
        l = int(math.log(n, 10)) + 1
        nums = deque([0, 0])

        for _ in range(l):
            dig = n % 10
            n //= 10

            if dig >= nums[-1]:
                nums.append(dig)
                nums.popleft()
            elif dig >= nums[-2]:
                nums.insert(1, dig)
                nums.popleft()

        return nums[-1] * nums[-2]
            
