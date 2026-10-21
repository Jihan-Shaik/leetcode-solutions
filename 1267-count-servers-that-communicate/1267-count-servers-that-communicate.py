class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        c=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    if grid[i].count(1)>1 or any(grid[k][j]==1 and k!=i for k in range(len(grid))): c+=1
        return c