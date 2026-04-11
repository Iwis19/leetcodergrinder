class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        """
        common algorithm: (try to be able to brain this out in the future)

        90 degrees clockwise - flip vertically, transpose horizontally
        90 degrees counterclockwise - flip horizontally, transpose vertically

        *transpose means reflect across diagonal

        0 ms runtime beats 100
        """

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
