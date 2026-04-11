class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        """
        in place rotation solution, came from 48. rotate image :)

        1. basically just flipped vertically, then transposed, then used this 90 deg clockwise rotations x 4 with a for loop to check if mat ever == target
        2. return results

        0 ms runtime beats 100
        """
        
        def rotate_arr_clockwise(matrix):
            
            n = len(matrix)
            top = 0
            bottom = n-1
             
            while top < bottom:

                matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
                top += 1
                bottom -= 1

            for i in range(n):
                for j in range(i+1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
        #0 1 2 3 
        if mat == target: return True

        for i in range(3):
            rotate_arr_clockwise(mat)
            if mat == target:
                return True

        return False
