class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        a=[[0]*len(matrix) for a in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                a[j][i]=matrix[i][j]
        return a