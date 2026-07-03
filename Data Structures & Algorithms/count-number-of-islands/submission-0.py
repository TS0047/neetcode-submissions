class Solution:
    def numIslands(self, grid):
        def bounds(r,c):
            return 0<=r<len(grid) and 0<=c<len(grid[0])
        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
        def dfs(i,j):
            grid[i][j]='2'
            for dr,dc in dirs:
                r,c = i+dr,j+dc
                if bounds(r,c) and grid[r][c]=='1':
                    dfs(r,c)
        islands=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    islands+=1
                    dfs(i,j)
        return islands

                


        