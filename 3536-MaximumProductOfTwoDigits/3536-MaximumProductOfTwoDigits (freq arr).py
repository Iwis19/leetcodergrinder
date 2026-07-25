class Solution:
    def maxProduct(self, n: int) -> int:

        """
        wew got this down too pretty quick tbh, better than last 1
        """
        
        l = int(math.log(n, 10)) + 1
        freq = [0] * 10

        for i in range(l):
            dig = n%10
            n//=10

            freq[dig] += 1

        digs = [-1, -1]

        for i in range(2):
            for j in range(9, -1, -1):
                if freq[j] != 0:
                    digs[i] = j
                    freq[j] -= 1
                    break

        return digs[0] * digs[1]
            
            
