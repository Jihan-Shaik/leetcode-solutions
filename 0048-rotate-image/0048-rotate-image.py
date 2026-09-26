class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        a=[a[:] for a in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix)): matrix[i][j]=a[j][i]
        for i in range(len(matrix)): matrix[i]=matrix[i][::-1]