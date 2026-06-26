class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        for i in range(size-1):
            for j in range(i,size):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(size):
            matrix[i].reverse()