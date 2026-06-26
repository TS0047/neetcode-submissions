class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        for i in range(size):
            for j in range(i,size):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for k in range(size):
            matrix[k].reverse()