class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        answer=matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==-1: answer[i][j]=max(a[j] for a in matrix)
        return answer