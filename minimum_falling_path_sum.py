#Time Complexity - O(n^2)
#Space Complexity - O(1)

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix or len(matrix) == 0:
            return 0

        n = len(matrix)
        for i in range(n-2,-1,-1):
            for j in range(n):
                if j == 0:
                    matrix[i][j] = matrix[i][j] + min(matrix[i+1][j], matrix[i+1][j+1])
                elif j == n -1:
                    matrix[i][j] = matrix[i][j] + min(matrix[i+1][j],matrix[i+1][j-1])
                else:
                    matrix[i][j] = matrix[i][j] + min(matrix[i+1][j], min(matrix[i+1][j-1] , matrix[i+1][j+1]))

        minimum = float('inf')
        for j in range(0,n):
            minimum = min(minimum,matrix[0][j])
        
        return minimum
            