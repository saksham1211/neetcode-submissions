class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols  = len(matrix[0])
        newMatrix=[[0]*rows for _ in range(cols)]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                newMatrix[c][r] = matrix[r][c]

        return newMatrix