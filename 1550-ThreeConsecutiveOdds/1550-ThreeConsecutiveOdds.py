class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        def isOdd(n:int) -> bool:
            if n%2 == 1:
                return True
            return False

        for i in range(len(arr)-2):
            if isOdd(arr[i]) and isOdd(arr[i+1]) and isOdd(arr[i+2]):
                return True

        return False
            

        
