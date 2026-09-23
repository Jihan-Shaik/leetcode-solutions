class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        c=0
        for i in range(len(mat)): c+=mat[i][i]+mat[i][len(mat)-i+-1]
        if len(mat)%2==0: return c
        else: return c-mat[(len(mat)-1)//2][(len(mat)-1)//2]